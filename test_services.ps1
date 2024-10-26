# Test de servicios
Write-Host "Probando servicios..." -ForegroundColor Green

# Test Servicio de Usuarios
try {
    $usersResponse = Invoke-RestMethod -Uri "http://localhost:5000/api/usuarios" -Method Get
    Write-Host "`nServicio de Usuarios:" -ForegroundColor Yellow
    $usersResponse.data | ConvertTo-Json
} catch {
    Write-Host "No se pudo conectar al servicio de usuarios." -ForegroundColor Red
}

# Test Servicio de Pedidos
try {
    $ordersResponse = Invoke-RestMethod -Uri "http://localhost:5001/api/pedidos" -Method Get
    Write-Host "`nServicio de Pedidos:" -ForegroundColor Yellow
    $ordersResponse.data | ConvertTo-Json
} catch {
    Write-Host "No se pudo conectar al servicio de pedidos." -ForegroundColor Red
}
