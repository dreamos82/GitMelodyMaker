from converters.modconverter import  ModConverter
class ConverterFactory:
    def get_converter(self, convertertype):
        if(convertertype == "mod"):
            return ModConverter()

