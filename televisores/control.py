class Control:
    _tv = None

    def enlazar(self, tv):
        self._tv = tv
        tv.setControl(self)

    def getTv(self):
        return self._tv
    
    def setTv(self, tv):
        self._tv = tv

    def turnOn(self) -> None:
        self._tv.turnOn()

    def turnOff(self) -> None:
        self._tv.turnOff()

    def canalUp(self) -> None:
        self._canal.canalUp()
    
    def canalDown(self) -> None:
        self._canal.canalDown()

    def volumenUp(self) -> None:
        self._volumen.volumenUp()

    def volumenDown(self) -> None:
        self._volumen.volumenDown()

    def setCanal(self, canal= int) -> None:
        self._canal.setCanal(canal)

    def setVolumen(self, volumen = int) -> None:
        self._volumen.setVolumen(volumen)

    
        