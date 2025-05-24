pkgname=calculadora-vhartz
pkgver=1.0
pkgrel=1
pkgdesc="Calculadora gráfica simples em Python com Tkinter"
arch=('any')
url="https://github.com/seuusuario/calculadora-vhartz"
license=('MIT')
depends=('python' 'tk')
source=('calculadora.py' 'calculadora-vhartz.desktop' 'calculadora-vhartz.png')
md5sums=('SKIP' 'SKIP' 'SKIP')

package() {
  install -Dm755 calculadora.py "$pkgdir/opt/calculadora-vhartz/calculadora.py"
  install -Dm755 calculadora-vhartz.desktop "$pkgdir/usr/share/applications/calculadora-vhartz.desktop"
  install -Dm644 calculadora-vhartz.png "$pkgdir/usr/share/icons/hicolor/128x128/apps/calculadora-vhartz.png"
  echo -e '#!/bin/bash\npython3 /opt/calculadora-vhartz/calculadora.py' > "$pkgdir/usr/local/bin/calculadora-vhartz"
  chmod +x "$pkgdir/usr/local/bin/calculadora-vhartz"
}
