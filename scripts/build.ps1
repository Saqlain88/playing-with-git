$ErrorActionPreference = "Stop"

if (Test-Path "build"){
    Remove-Item "build" -Recurse -Force
}

New-Item -ItemType Directory -Path "build" | Out-Null

Copy-Item "app" "build/app" -Recurse
Copy-Item "requirements.txt" "build/requirements.txt"
Copy-Item "README.md" "build/README.md"

Write-Host "Build completed successfully."