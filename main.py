from numpy import asarray
from PIL import Image
import colorama as cl
import io

cl.init()

def list_to_hex(list_image):
	res = ""
	for i in list_image:
		for j in i:
			hexd = [format(j[0], "x"), \
				    format(j[1], "x"), \
				    format(j[2], "x")  ]
			hexd[0] = hexd[0] if len(hexd[0]) == 2 else "0" + hexd[0]
			hexd[1] = hexd[1] if len(hexd[1]) == 2 else "0" + hexd[1]
			hexd[2] = hexd[2] if len(hexd[2]) == 2 else "0" + hexd[2]
			res += hexd[0] + hexd[1] + hexd[2]
	return bytes.fromhex(res)

images = (
	("bg.png", 320, 240),
	("icon1_0.png", 64, 64),
	("icon2_0.png", 64, 64),
	("icon3_0.png", 64, 64),
	("icon4_0.png", 64, 64),
	("icon5_0.png", 64, 64),
	("icon6_0.png", 64, 64),
	("icon7_0.png", 64, 64),
	("icon8_0.png", 64, 64),
	("icon9_0.png", 64, 64),
	("miniicon_3gp.png", 38, 38),
	("miniicon_akv.png", 38, 38),
	("miniicon_avi.png", 38, 38),
	("miniicon_bmp.png", 38, 38),
	("miniicon_doc.png", 38, 38),
	("miniicon_gif.png", 38, 38),
	("miniicon_jpg.png", 38, 38),
	("miniicon_mid.png", 38, 38),
	("miniicon_mp3.png", 38, 38),
	("miniicon_mp4.png", 38, 38),
	("miniicon_pdf.png", 38, 38),
	("miniicon_png.png", 38, 38),
	("miniicon_txt.png", 38, 38),
	("miniicon_wma.png", 38, 38),
	("miniicon_xls.png", 38, 38),
	("miniicon_wav.png", 38, 38),
	("miniicon_lrc.png", 38, 38),
	("miniicon_amr.png", 38, 38),
	("miniicon_mpeg.png", 38, 38),
	("miniicon_adif.png", 38, 38),
	("miniicon_adts.png", 38, 38),
	("miniicon_m4a.png", 38, 38),
	("miniicon_map.png", 38, 38),
	("miniicon_nes.png", 38, 38),
	("miniicon_alt.png", 38, 38),
	("miniicon_folder.png", 38, 38),
	("miniicon_folder_i.png", 38, 38),
	("miniicon_up_arrow.png", 38, 38),
	("miniicon_drive.png", 38, 38),
	("icon1_1.png", 87, 87),
	("icon1_2.png", 87, 87),
	("icon2_1.png", 87, 87),
	("icon2_2.png", 87, 87),
	("icon3_1.png", 87, 87),
	("icon3_2.png", 87, 87),
	("icon4_1.png", 87, 87),
	("icon4_2.png", 87, 87),
	("icon5_1.png", 87, 87),
	("icon5_2.png", 87, 87),
	("icon6_1.png", 87, 87),
	("icon6_2.png", 87, 87),
	("icon7_1.png", 87, 87),
	("icon7_2.png", 87, 87),
	("icon8_1.png", 87, 87),
	("icon8_2.png", 87, 87),
	("icon9_1.png", 87, 87),
	("icon9_2.png", 87, 87),
)

for i in images:
	try:
		image = Image.open(f"assets/{i[0]}")
	except FileNotFoundError:
		print(f"FE: Image \"{i[0]}\" is not found in \"assets\" folder!")
		exit(1)

	if image.size != i[1:3]:
		print(f"FE: Image \"{i[0]}\" is not {i[1]}x{i[2]}!")
		exit(1)

# self.im = Image.new('RGB', image.size, (255, 255, 255))
# self.im.paste(image, None)

	if image.mode == "RGB":
		array = asarray(image).tolist()
	else:
		print(f"{cl.Fore.WHITE}{cl.Back.YELLOW}W:{cl.Style.RESET_ALL} Image \"{i[0]}\" has non-RGB mode, converting it...")
		converted = Image.new("RGB", image.size, (255, 0, 255))
		converted.paste(image, None)
		array = asarray(converted).tolist()

	exec(f"{i[0].split('.')[0]} = list_to_hex(array)")

with open("AkResData.Bin", "r+b") as file:
	file.seek(0x3550)
	file.write(b"  ON")
	file.seek(0x3564)
	file.write(b"  OFF")
	file.seek(0x68502)
	file.write(bg)
	file.seek(0xb4c92)
	file.write(bg)
	file.seek(0xf6de2)
	file.write(icon1_0)
	file.seek(0x104f62)
	file.write(icon2_0)
	file.seek(0x1130e2)
	file.write(icon3_0)
	file.seek(0x121262)
	file.write(icon4_0)
	file.seek(0x12f3e2)
	file.write(icon5_0)
	file.seek(0x13d562)
	file.write(icon6_0)
	file.seek(0x14b6e2)
	file.write(icon7_0)
	file.seek(0x159862)
	file.write(icon8_0)
	file.seek(0x1679e2)
	file.write(icon9_0)
	file.seek(0x4394E)
	file.write(miniicon_3gp)
	file.seek(0x47A4A)
	file.write(miniicon_akv)
	file.seek(0x48B3E)
	file.write(miniicon_avi)
	file.seek(0x49C32)
	file.write(miniicon_bmp)
	file.seek(0x4AD26)
	file.write(miniicon_doc)
	file.seek(0x4BE1A)
	file.write(miniicon_gif)
	file.seek(0x4CF0E)
	file.write(miniicon_jpg)
	file.seek(0x4E002)
	file.write(miniicon_mid)
	file.seek(0x4F0F6)
	file.write(miniicon_mp3)
	file.seek(0x501EA)
	file.write(miniicon_mp4)
	file.seek(0x512DE)
	file.write(miniicon_pdf)
	file.seek(0x523D2)
	file.write(miniicon_png)
	file.seek(0x534C6)
	file.write(miniicon_txt)
	file.seek(0x545BA)
	file.write(miniicon_wma)
	file.seek(0x556AE)
	file.write(miniicon_xls)
	file.seek(0x567A2)
	file.write(miniicon_wav)
	file.seek(0x57896)
	file.write(miniicon_lrc)
	file.seek(0x5898A)
	file.write(miniicon_amr)
	file.seek(0x59A7E)
	file.write(miniicon_mpeg)
	file.seek(0x5AB72)
	file.write(miniicon_adif)
	file.seek(0x5BC66)
	file.write(miniicon_adts)
	file.seek(0x5CD5A)
	file.write(miniicon_m4a)
	file.seek(0x5DE4E)
	file.write(miniicon_map)
	file.seek(0x5EF42)
	file.write(miniicon_nes)
	file.seek(0x60036)
	file.write(miniicon_alt)
	file.seek(0x64132)
	file.write(miniicon_folder)
	file.seek(0x65226)
	file.write(miniicon_folder_i)
	file.seek(0x6631B)
	file.write(miniicon_up_arrow)
	file.seek(0x6740E)
	file.write(miniicon_drive)
	file.seek(0xF9DEA)
	file.write(icon1_1) 
	file.seek(0xFF6A6)
	file.write(icon1_2) 
	file.seek(0x107F6A)
	file.write(icon2_1) 
	file.seek(0x10D826)
	file.write(icon2_2) 
	file.seek(0x1160EA)
	file.write(icon3_1) 
	file.seek(0x11B9A6)
	file.write(icon3_2) 
	file.seek(0x12426A)
	file.write(icon4_1) 
	file.seek(0x129B26)
	file.write(icon4_2) 
	file.seek(0x1323EA)
	file.write(icon5_1) 
	file.seek(0x137CA6)
	file.write(icon5_2) 
	file.seek(0x14056A)
	file.write(icon6_1) 
	file.seek(0x145E26)
	file.write(icon6_2) 
	file.seek(0x14E6EA)
	file.write(icon7_1) 
	file.seek(0x153FA6)
	file.write(icon7_2) 
	file.seek(0x15C86A)
	file.write(icon8_1) 
	file.seek(0x162126)
	file.write(icon8_2) 
	file.seek(0x16A9EA)
	file.write(icon9_1) 
	file.seek(0x1702A6)
	file.write(icon9_2) 
