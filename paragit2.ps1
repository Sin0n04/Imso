New-Item -Path 'c:\' -ItemType 'directory' -Name 'ejercicio'
Set-Location 'c:\ejercicio'
New-Item hola.txt
Copy-Item hola.txt hola.bak
