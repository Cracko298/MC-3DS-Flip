import os
import struct
from io import BytesIO
from PIL import Image

class TextureReplacer:
    def __init__(self, parent):
        self.current_file = ""
        self.parent_form = parent
        self.mip_sel = 0
        self.bch = None

        self.texture_type_list = [
            "rgba8",
            "rgb8",
            "rgba5551",
            "rgb565",
            "rgba4",
            "la8",
            "hilo8",
            "l8",
            "a8",
            "la4",
            "l4",
            "a4",
            "etc1",
            "etc1a4"
        ]
        self.mip_select_list = ["1", "2", "3", "4", "5", "6"]

    def open(self):
        input_file = "gingerbread.3dst"  # Replace with your input file path
        if os.path.isfile(input_file):
            with open(input_file, "rb") as file_stream:
                self.open_file(file_stream)

    def open_file(self, file_stream):
        magic = self.peek(file_stream, 4)
        if magic == b"\x00\x01\x00\x00":
            self.current_file = file_stream
            self.bch = LoadedBCH(is_bch=False)
            self.bch.mips.append(MIPlayer())
            self.pack_pnk(file_stream, self.bch)

        if magic == b"PK\x0c\x04":
            self.current_file = file_stream
            self.bch = LoadedBCH(is_bch=False)
            self.bch.mips.append(MIPlayer())
            self.bch.mips[0].textures.append(self.load_pkm(file_stream))

        magic = self.get_magic(file_stream, 2)
        if magic in ["PC", "CM"]:
            self.bch = LoadedBCH(is_bch=False)
            self.current_file = file_stream
            file_stream.seek(2, 1)
            num1 = struct.unpack("<H", file_stream.read(2))[0]
            for index in range(num1):
                file_stream.seek(4 + index * 4, 0)
                offset = struct.unpack("<I", file_stream.read(4))[0]
                num2 = struct.unpack("<I", file_stream.read(4))[0] - offset
                position = file_stream.tell()
                file_stream.seek(offset, 0)
                if magic == "CM" and index == 0:
                    self.pack_pnk(file_stream, self.bch)
                if num2 > 4 and magic == "PC" and self.peek(file_stream, 4) == b"PK\x0c\x04":
                    self.bch.mips[0].textures.append(self.load_pkm(file_stream))

        if self.read_string(file_stream, 0) == "BCH":
            self.current_file = file_stream
            file_stream.seek(4, 1)
            num3 = struct.unpack("<B", file_stream.read(1))[0]
            num4 = struct.unpack("<B", file_stream.read(1))[0]
            num5 = struct.unpack("<H", file_stream.read(2))[0]
            offset1 = struct.unpack("<I", file_stream.read(4))[0]
            num6 = struct.unpack("<I", file_stream.read(4))[0]
            num7 = struct.unpack("<I", file_stream.read(4))[0]
            num8 = struct.unpack("<I", file_stream.read(4))[0]
            if num3 > 32:
                struct.unpack("<I", file_stream.read(4))[0]
            num10 = struct.unpack("<I", file_stream.read(4))[0]
            num11 = struct.unpack("<I", file_stream.read(4))[0]
            num12 = struct.unpack("<I", file_stream.read(4))[0]
            num13 = struct.unpack("<I", file_stream.read(4))[0]
            num14 = struct.unpack("<I", file_stream.read(4))[0]
            if num3 > 32:
                struct.unpack("<I", file_stream.read(4))[0]
            num16 = struct.unpack("<I", file_stream.read(4))[0]
            file_stream.seek(offset1, 0)
            num17 = struct.unpack("<I", file_stream.read(4))[0]
            num18 = struct.unpack("<I", file_stream.read(4))[0]
            file_stream.seek(offset1 + 36, 0)
            num19 = struct.unpack("<I", file_stream.read(4))[0] + offset1
            num20 = struct.unpack("<I", file_stream.read(4))[0]
            self.bch = LoadedBCH(is_bch=True)
            self.bch.mips = [MIPlayer() for _ in range(6)]
            self.mip_sel = 0
            for index1 in range(num20):
                file_stream.seek(num19 + index1 * 4, 0)
                file_stream.seek(struct.unpack("<I", file_stream.read(4))[0] + offset1, 0)
                loaded_texture = self.load_texture(file_stream)
                self.bch.mips[0].textures.append(loaded_texture)

    def find_type(self):
        texture_type = self.TextureTypeDrop.Text.lower()
        if texture_type == "rgba8":
            return RenderBase.OTextureFormat.rgba8
        elif texture_type == "rgb8":
            return RenderBase.OTextureFormat.rgb8
        elif texture_type == "rgba5551":
            return RenderBase.OTextureFormat.rgba5551
        elif texture_type == "rgb565":
            return RenderBase.OTextureFormat.rgb565
        elif texture_type == "rgba4":
            return RenderBase.OTextureFormat.rgba4
        elif texture_type == "la8":
            return RenderBase.OTextureFormat.la8
        elif texture_type == "hilo8":
            return RenderBase.OTextureFormat.hilo8
        elif texture_type == "l8":
            return RenderBase.OTextureFormat.l8
        elif texture_type == "a8":
            return RenderBase.OTextureFormat.a8
        elif texture_type == "la4":
            return RenderBase.OTextureFormat.la4
        elif texture_type == "l4":
            return RenderBase.OTextureFormat.l4
        elif texture_type == "a4":
            return RenderBase.OTextureFormat.a4
        elif texture_type == "etc1":
            return RenderBase.OTextureFormat.etc1
        elif texture_type == "etc1a4":
            return RenderBase.OTextureFormat.etc1a4
        else:
            raise Exception("Invalid texture type: {}".format(texture_type))

    def update_texture_list(self):
        self.TextureList.flush()
        self.PicPreview.Image = None
        for texture in self.bch.mips[self.mip_sel].textures:
            self.TextureList.addItem(texture.texture.name)
        self.TextureList.Refresh()

    def texture_list_selected_index_changed(self):
        if self.TextureList.SelectedIndex == -1:
            return
        texture = self.bch.mips[self.mip_sel].textures[self.TextureList.SelectedIndex]
        self.PicPreview.Image = texture.texture.texture
        self.TextureTypeDrop.Text = texture.type.name.lower()
        self.TextureTypeDrop.Enabled = False

    def texture_type_drop_change(self):
        if self.TextureList.SelectedIndex == -1:
            return
        texture = self.bch.mips[self.mip_sel].textures[self.TextureList.SelectedIndex]
        self.bch.mips[self.mip_sel].textures.pop(self.TextureList.SelectedIndex)
        texture.type = self.find_type()
        self.bch.mips[self.mip_sel].textures.insert(self.TextureList.SelectedIndex, texture)

    def btn_export_click(self):
        if self.TextureList.SelectedIndex == -1:
            return
        texture = self.bch.mips[self.mip_sel].textures[self.TextureList.SelectedIndex]
        with SaveFileDialog() as saveFileDialog:
            saveFileDialog.Filter = "Image|*.png"
            if saveFileDialog.ShowDialog() == DialogResult.OK:
                texture.texture.texture.save(saveFileDialog.FileName)

    def btn_export_all_click(self):
        if self.TextureList.SelectedIndex == -1:
            return
        with FolderBrowserDialog() as folderBrowserDialog:
            if folderBrowserDialog.ShowDialog() == DialogResult.OK:
                for texture in self.bch.mips[self.mip_sel].textures:
                    file_path = os.path.join(folderBrowserDialog.SelectedPath, texture.texture.name + ".png")
                    texture.texture.texture.save(file_path)

    def btn_replace_click(self):
        if self.TextureList.SelectedIndex == -1:
            return
        with OpenFileDialog() as openFileDialog:
            openFileDialog.Filter = "Image|*.png"
            if openFileDialog.ShowDialog() == DialogResult.OK:
                texture = self.bch.mips[self.mip_sel].textures[self.TextureList.SelectedIndex]
                self.bch.mips[self.mip_sel].textures.pop(self.TextureList.SelectedIndex)
                bitmap = Image.open(openFileDialog.FileName)
                texture.texture.texture = bitmap
                texture.modified = True
                self.bch.mips[self.mip_sel].textures.insert(self.TextureList.SelectedIndex, texture)
                self.PicPreview.Image = bitmap

class OBCHTextureReplacer:
    def __init__(self):
        self.bch = None
        self.mip_sel = 0
        self.current_file = ""
        self.components = None
        self.PicPreview = None
        self.TextureList = None
        self.BtnReplaceAll = None
        self.BtnReplace = None
        self.BtnExportAll = None
        self.BtnExport = None
        self.SplitPanel = None
        self.ButtonsLayout = None
        self.TopMenu = None
        self.MenuFile = None
        self.MenuOpen = None
        self.MenuSave = None
        self.MenuSaveAndPreview = None
        self.MenuSeparator0 = None
        self.MenuExit = None
        self.TextureTypeDrop = None
        self.MipSelect = None
        self.initialize_components()

    def initialize_components(self):
        # Initialize all the UI components here (e.g., buttons, menus, etc.)
        pass

    def btn_replace_all_click(self):
        if self.bch is None:
            return
        with FolderBrowserDialog() as folderBrowserDialog:
            if folderBrowserDialog.ShowDialog() != DialogResult.OK:
                return
            files = Directory.GetFiles(folderBrowserDialog.SelectedPath)
            for index, texture in enumerate(self.bch.mips[self.mip_sel].textures):
                for file_path in files:
                    file_name = Path.GetFileNameWithoutExtension(file_path)
                    if file_name.lower() == texture.texture.name.lower():
                        self.bch.mips[self.mip_sel].textures.pop(index)
                        bitmap = Bitmap(file_path)
                        texture.texture.texture = bitmap
                        texture.modified = True
                        self.bch.mips[self.mip_sel].textures.insert(index, texture)
                        if self.TextureList.SelectedIndex == index:
                            self.PicPreview.Image = bitmap

    def save(self):
        with FileStream(self.current_file, FileMode.Open) as fileStream:
            binaryReader = BinaryReader(fileStream)
            binaryWriter = BinaryWriter(fileStream)
            for index, texture in enumerate(self.bch.mips[self.mip_sel].textures):
                if texture.modified:
                    new_data = self.align(TextureCodec.encode(texture.texture.texture, texture.type))
                    length = len(new_data)
                    self.replace_data(fileStream, texture.offset, self.return_size(texture.type, texture.texture.texture.Width, texture.texture.texture.Height), new_data)
                    texture.modified = False
                    self.update_texture(index, texture)
        MessageBox.Show("Done!", "Information", MessageBoxButtons.OK, MessageBoxIcon.Asterisk)

    def align(self, input):
        length = len(input)
        while length & 0x7F:
            length += 1
        dst = bytearray(length)
        Buffer.BlockCopy(input, 0, dst, 0, len(input))
        return dst

    def replace_command(self, data, output, new_val):
        data.Seek(-8, SeekOrigin.Current)
        output.Write(new_val)
        data.Seek(4, SeekOrigin.Current)

    def replace_data(self, data, offset, length, new_data):
        data.Seek(offset, SeekOrigin.Begin)
        data.Write(new_data, 0, length)

    def update_address(self, data, input, output, diff):
        num = input.ReadUInt32() + diff
        data.Seek(-4, SeekOrigin.Current)
        output.Write(num)

    def update_texture(self, index, new_tex):
        self.bch.mips[self.mip_sel].textures.pop(index)
        self.bch.mips[self.mip_sel].textures.insert(index, new_tex)

    def mip_layer_changed(self, sender, e):
        self.mip_sel = int(self.MipSelect.Text) - 1
        self.update_texture_list()

    def find_type(self):
        return RenderBase.OTextureFormat[self.TextureTypeDrop.Text.upper()]

    def texture_list_selected_index_changed(self, sender, e):
        if self.TextureList.SelectedIndex == -1:
            return
        texture = self.bch.mips[self.mip_sel].textures[self.TextureList.SelectedIndex]
        self.PicPreview.Image = texture.texture.texture
        self.TextureTypeDrop.Text = texture.type.name.lower()
        self.TextureTypeDrop.Enabled = False

    def texture_type_drop_change(self, sender, e):
        if self.TextureList.SelectedIndex == -1:
            return
        texture = self.bch.mips[self.mip_sel].textures[self.TextureList.SelectedIndex]
        self.bch.mips[self.mip_sel].textures.pop(self.TextureList.SelectedIndex)
        texture.type = self.find_type()
        self.bch.mips[self.mip_sel].textures.insert(self.TextureList.SelectedIndex, texture)

    def btn_export_click(self, sender, e):
        if self.TextureList.SelectedIndex == -1:
            return
        texture = self.bch.mips[self.mip_sel].textures[self.TextureList.SelectedIndex]
        with SaveFileDialog() as saveFileDialog:
            saveFileDialog.Filter = "Image|*.png"
            if saveFileDialog.ShowDialog() == DialogResult.OK:
                texture.texture.texture.save(saveFileDialog.FileName)

    def btn_export_all_click(self, sender, e):
        if self.TextureList.SelectedIndex == -1:
            return
        with FolderBrowserDialog() as folderBrowserDialog:
            if folderBrowserDialog.ShowDialog() == DialogResult.OK:
                for texture in self.bch.mips[self.mip_sel].textures:
                    file_path = os.path.join(folderBrowserDialog.SelectedPath, texture.texture.name + ".png")
                    texture.texture.texture.save(file_path)

    def btn_replace_click(self, sender, e):
        if self.TextureList.SelectedIndex == -1:
            return
        with OpenFileDialog() as openFileDialog:
            openFileDialog.Filter = "Image|*.png"
            if openFileDialog.ShowDialog() == DialogResult.OK:
                texture = self.bch.mips[self.mip_sel].textures[self.TextureList.SelectedIndex]
                self.bch.mips[self.mip_sel].textures.pop(self.TextureList.SelectedIndex)
                bitmap = Image.open(openFileDialog.FileName)
                texture.texture.texture = bitmap
                texture.modified = True
                self.bch.mips[self.mip_sel].textures.insert(self.TextureList.SelectedIndex, texture)
                self.PicPreview.Image = bitmap

from collections import namedtuple
from enum import Enum
from PIL import Image

class OBCHTextureReplacer:
    def __init__(self):
        self.bch = None
        self.mip_sel = 0
        self.current_file = ""
        self.components = None
        self.PicPreview = None
        self.TextureList = None
        self.BtnReplaceAll = None
        self.BtnReplace = None
        self.BtnExportAll = None
        self.BtnExport = None
        self.SplitPanel = None
        self.ButtonsLayout = None
        self.TopMenu = None
        self.MenuFile = None
        self.MenuOpen = None
        self.MenuSave = None
        self.MenuSaveAndPreview = None
        self.MenuSeparator0 = None
        self.MenuExit = None
        self.TextureTypeDrop = None
        self.MipSelect = None
        self.loaded_texture = namedtuple("loadedTexture", ["modified", "gpuCommandsOffset", "gpuCommandsWordCount", "offset", "length", "texture", "type"])
        self.loaded_bch = namedtuple("loadedBCH", ["isBCH", "mainHeaderOffset", "gpuCommandsOffset", "dataOffset", "relocationTableOffset", "relocationTableLength", "mips"])
        self.mip_layer = namedtuple("MIPlayer", ["textures"])
        self.initialize_components()

    # ... (rest of the code)

    class RenderBase(Enum):
        OTextureFormat = {
            "RGBA8": 0,
            "RGB8": 1,
            "RGB565": 2,
            "RGBA5551": 3,
            "RGBA4": 4,
            "LA8": 5,
            "HILO8": 6,
            "L8": 7,
            "A8": 8,
            "LA4": 9,
            "L4": 10,
            "A4": 11,
            "ETC1": 12,
            "ETC1A4": 13,
            "L4_REVERSED": 14,
            "A4_REVERSED": 15,
            "ETC1_REVERSED": 16,
            "ETC1A4_REVERSED": 17,
            "L8_REVERSED": 18,
            "A8_REVERSED": 19,
            "LA4_REVERSED": 20,
            "HILO8_REVERSED": 21,
            "RGBA16F": 22,
            "RGB8A4": 23,
            "A1B5G5R5": 24,
            "B5G6R5": 25,
            "BC4": 26,
            "BC5": 27,
            "RPZA": 28,
            "DXT1": 29,
            "DXT3": 30,
            "DXT5": 31,
            "CTX1": 32,
        }

    def menu_open_click(self, sender, e):
        with OpenFileDialog() as openFileDialog:
            openFileDialog.Filter = "Binary Custom Header Files|*.bch"
            if openFileDialog.ShowDialog() == DialogResult.OK:
                self.current_file = openFileDialog.FileName
                self.bch = self.load_bch(openFileDialog.FileName)
                if self.bch.isBCH:
                    self.update_textures_list()

    def menu_save_click(self, sender, e):
        if self.bch is None:
            return
        self.save()

    def menu_save_and_preview_click(self, sender, e):
        if self.bch is None:
            return
        self.save()
        # Add code for previewing the modified textures here

    def menu_exit_click(self, sender, e):
        self.Close()

    def texture_type_drop_change(self, sender, e):
        if self.TextureList.SelectedIndex == -1:
            return
        texture = self.bch.mips[self.mip_sel].textures[self.TextureList.SelectedIndex]
        self.bch.mips[self.mip_sel].textures.pop(self.TextureList.SelectedIndex)
        texture.type = self.find_type()
        self.bch.mips[self.mip_sel].textures.insert(self.TextureList.SelectedIndex, texture)

    def obch_texture_replacer_key_down(self, sender, e):
        if e.KeyCode == Keys.O and e.Modifiers == Keys.Control:
            self.menu_open_click(sender, e)
        elif e.KeyCode == Keys.S and e.Modifiers == Keys.Control:
            self.menu_save_click(sender, e)
        elif e.KeyCode == Keys.P and e.Modifiers == Keys.Control:
            self.menu_save_and_preview_click(sender, e)
        elif e.KeyCode == Keys.Escape:
            self.menu_exit_click(sender, e)

    def load_bch(self, file_path):
        bch = self.loaded_bch()
        # Load the BCH file and populate the bch object here
        # You will need to implement the logic for parsing the BCH file
        return bch

    def update_textures_list(self):
        # Update the TextureList based on the loaded BCH data
        pass

    def return_size(self, texture_type, width, height):
        # Implement logic to return the size based on texture_type, width, and height
        pass

# Create and run the form
form = OBCHTextureReplacer()
Application.Run(form)
