import random
import struct
import binascii


class ColorCode():

    # init
    def __init__(self):
        self.hex_code = ''
        self.rgb_code = [3]
        self.hsv_code = [3]
        self.cmyk_code = [4]

    def generate_hex(self):
        
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F']
        
        # choose between number or alphabet in sequence, then generate
        hex_list = ['#']
        
        # although possible, for loop is cleaner than list comprehension
        for x in range(0, 6):

            if random.randint(0, 2) % 2 is 0:
                hex_list.append(alphabet[random.randint(0, len(alphabet) - 1)])
            else:
                hex_list.append(str(random.randint(0, 9)))
        
        self.hex_code = ''.join(hex_list)
        
        return self.hex_code

    def generate_rgb(self):
        
        rgb_list = [random.randint(0, 256) for x in range(0, 3)]
        self.rgb_code = rgb_list
        
        return self.rgb_code

    def generate_hsv(self):

        hsv_list = [random.randint(0, 101) if x >= 1 else random.randint(0, 400) for x in range(0,3)]
        self.hsv_code = hsv_list

        return self.hsv_code

    def generate_cmyk(self):

        cmyk_list = [random.randint(0, 101) for x in range(0, 4)]
        self.cmyk_code = cmyk_list
        
        return self.cmyk_code

    def generate_color(self):

        self.generate_hex()

        return self.hex_code

    def hex_to_rbg(self):

        temp_hex = self.hex_code.lstrip('#')
        # hex_length = len(temp_hex)
        #
        # # rgb uses base 16
        # new_rgb = [int(temp_hex[i:i + hex_length // 3], 16) for i in range(0, hex_length, hex_length // 3)]

        new_rgb = struct.unpack('BBB', bytes.fromhex(temp_hex))

        return new_rgb

    def rgb_to_hex(self):

        temp_rgb = self.rgb_code
        new_hex = binascii.hexlify(struct.pack('BBB', *temp_rgb)).decode('utf-8')

        return new_hex

