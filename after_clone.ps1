Write-Host "Creating virtual environment..."
python -m venv env
.\env\Scripts\activate.ps1

Write-Host "Installing dependencies..."
pip install -r requirements.txt

Write-Host "Creating .env file for environment variables..."
Get-Content .env.example | Set-Content .env

Write-Host "Done!"
