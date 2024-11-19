class Control:
    _tv = None

    def enlazar(self, tv):
        self._tv = tv
        tv.setControl(self)

    def getTv(self):
        return self._tv
    
    def setTv(self, tv):
        self._tv = tv

    def turnOn(self):
        self._tv.turnOn()

    def turnOff(self):
        self._tv.turnOff()

    def canalUp(self):
        self._canal.canalUp()
    
    def canalDown(self):
        self._canal.canalDown()

    def volumenUp(self):
        self._volumen.volumenUp()

    def volumenDown(self):
        self._volumen.volumenDown()

    def setCanal(self, canal= int):
        self._canal.setCanal(canal)

    def setVolumen(self, volumen = int):
        self._volumen.setVolumen(volumen)

    
        