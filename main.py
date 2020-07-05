import requests,json, time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

listKode = {"Bank BCA": "014", "Bank Mandiri": "008", "Bank BNI": "009", "Bank BNI Syariah": "427", "Bank BRI": "002", "Bank Syariah Mandiri": "451", "Bank CIMB Niaga": "022", "Bank CIMB Niaga Syariah": "022", "Bank Muamalat": "147", "Bank Tabungan Pensiunan Nasional (BTPN)": "213", "JENIUS": "213", "Bank BRI Syariah": "422", "Bank Tabungan Negara (BTN)": "200", "Permata Bank": "013", "Bank Danamon": "011", "Bank BII Maybank": "016", "Bank Mega": "426", "Bank Sinarmas": "153", "Bank Commonwealth": "950", "Bank OCBC NISP": "028", "Bank Bukopin": "441", "Bank BCA Syariah": "536", "Bank Lippo": "026", "Citibank": "031", "Indosat Dompetku": "789", "Telkomsel Tcash": "911", "Bank Jabar dan Banten (BJB)": "110", "Bank DKI": "111", "BPD DIY": "112", "Bank Jateng": "113", "Bank Jatim": "114", "BPD Jambi": "115", "BPD Aceh, BPD Aceh Syariah": "116", "Bank Sumut": "117", "Bank Nagari": "118", "Bank Riau": "119", "Bank Sumsel Babel": "120", "Bank Lampung": "121", "Bank Kalsel": "122", "Bank Kalimantan Barat": "123", "Bank Kalimantan Timur dan Utara": "124", "Bank Kalteng": "125", "Bank Sulsel dan Barat": "126", "Bank Sulut Gorontalo": "127", "Bank NTB, NTB Syariah": "128", "BPD Bali": "129", "Bank NTT": "130", "Bank Maluku Malut": "131", "Bank Papua": "132", "Bank Bengkulu": "133", "Bank Sulawesi Tengah": "134", "Bank Sultra": "135", "Bank Ekspor Indonesia": "003", "Bank Panin": "019", "Bank Arta Niaga Kencana": "020", "Bank UOB Indonesia": "023", "American Express Bank LTD": "030", "Citibank N.A": "031", "JP. Morgan Chase Bank, N.A": "032", "Bank of America, N.A": "033", "ING Indonesia Bank": "034", "Link Aja": "911", "Bank Artha Graha Internasional": "037", "Bank Credit Agricole Indosuez": "039", "The Bangkok Bank Comp. LTD": "040", "The Hongkong & Shanghai B.C. (Bank HSBC)": "041", "The Bank of Tokyo Mitsubishi UFJ LTD": "042", "Bank Sumitomo Mitsui Indonesia": "045", "Bank DBS Indonesia": "046", "Bank Resona Perdania": "047", "Bank Mizuho Indonesia": "048", "Standard Chartered Bank": "050", "Bank ABN Amro": "052", "Bank Keppel Tatlee Buana": "053", "Bank Capital Indonesia": "054", "Bank BNP Paribas Indonesia": "057", "Bank UOB Indonesia": "023", "Korea Exchange Bank Danamon": "059", "Bank BJB Syariah": "425", "Bank ANZ Indonesia": "061", "Deutsche Bank AG.": "067", "Bank Woori Indonesia": "068", "Bank OF China": "069", "Bank Bumi Arta": "076", "Bank Ekonomi": "087", "Bank Antardaerah": "088", "Bank Haga": "089", "Bank IFI": "093", "Bank JTRUST": "095", "Bank Mayapada": "097", "Bank Nusantara Parahyangan": "145", "Bank of India Indonesia": "146", "Bank Mestika Dharma": "151", "Bank Metro Express (Bank Shinhan Indonesia)": "152", "Bank Maspion Indonesia": "157", "Bank Hagakita": "159", "Bank Ganesha": "161", "Bank Windu Kentjana": "162", "Halim Indonesia Bank (Bank ICBC Indonesia)": "164", "Bank Harmoni International": "166", "Bank QNB Kesawan (Bank QNB Indonesia)": "167", "Bank Himpunan Saudara 1906": "212", "Bank Swaguna": "405", "Bank Jasa Jakarta": "472", "Bank Bisnis Internasional": "459", "Bank Sri Partha": "466", "Bank Bintang Manunggal": "484", "Bank MNC / Bank Bumiputera": "485", "Bank Yudha Bhakti": "490", "Bank BRI Agro": "494", "Bank Indomonex (Bank SBI Indonesia)": "498", "Bank Royal Indonesia": "501", "Bank Alfindo (Bank National Nobu)": "503", "Bank Syariah Mega": "506", "Bank Ina Perdana": "513", "Bank Harfa": "517", "Prima Master Bank": "520", "Bank Persyarikatan Indonesia": "521", "Bank Akita": "525", "Liman International Bank": "526", "Anglomas Internasional Bank": "531", "Bank Dipo International (Bank Sahabat Sampoerna)": "523", "Bank Kesejahteraan Ekonomi": "535", "Bank Artos IND": "542", "Bank Purba Danarta": "547", "Bank Multi Arta Sentosa": "548", "Bank Mayora Indonesia": "553", "Bank Index Selindo": "555", "Centratama Nasional Bank": "559", "Bank Victoria International": "566", "Bank Fama Internasional": "562", "Bank Mandiri Taspen Pos": "564", "Bank Harda": "567", "BPR KS": "688", "Bank Agris": "945", "Bank Merincorp": "946", "Bank Maybank Indocorp": "947", "Bank OCBC - Indonesia": "948", "Bank CTBC (China Trust) Indonesia": "949"}
pilihanBank = []
for key,index in listKode.items():
	pilihanBank += [key]
pilihanBank.sort()


def loadingNyo():
	textInfo = tk.StringVar()
	textInfo.set('Loading ...')
	loading = tk.Label(inUser, textvariable=textInfo,bg='#302f2b', fg='white').place(x=185, y=100)

	gasbro()
	textInfo.set('Succes')

def gasbro():
	# outUser.pack_forget()
	outUser.pack(fill=tk.X)
	bank = variable.get()
	noRek = variable2.get()
	
	try:
		int(noRek)
		if bank not in pilihanBank:
			messagebox.showwarning('Bank Not Found', 'Masukkan Nama Bank yang benar')
		else:
			
			bankKode=listKode[bank]
			webReq = 'http://api.makira.id/cek-norek?kodeBank='+bankKode+'&noRek='+noRek
			reqq = requests.get(webReq)
			response = reqq.json()
			if reqq.text == 'server error':
				messagebox.showwarning('Server Error', 'Server sedang error, silahkan coba sebentar lagi')
			elif response['status'] != '0000':
				messagebox.showerror('Not Found', 'Nomor Rekening anda tidak ditemukan di {}'.format(bank))
			else:
				messagebox.showinfo('Succes', 'Pencarian Sukses')
				infoDasar = tk.Label(outUser, text="No Bank : {}  No Rek : {}".format(bankKode,noRek),bg='#302f2b', fg='white').place(x=10, y=5)
				namaOrang = tk.Label(outUser, text="Nama :\n {}".format(response['data']['name']), fg='black',font=("Courier", 14)).place(x=5, y=35)
	except ValueError:
		messagebox.showerror('No Rekening', 'Harap masukkan Nomor rekening yang benar')
	# namaOrang.


if __name__ == '__main__':
	win = tk.Tk()
	win.title("Checking Rekening")
	win.geometry("420x220")
	win.resizable(False, False) 
	inUser = tk.Frame(win, bg='#302f2b',width=420, height=125)
	inUser.pack(fill=tk.X)
	outUser = tk.Frame(win, height=100)
	

	variable = tk.StringVar(win)
	variable.set('Bank Bengkulu')
	variable2 = tk.StringVar(win)
	variable2.set('1040205024762')

	labelRek = tk.Label(inUser, text="No Rekening : ",bg='#302f2b', fg='white').place(x=15, y=15)

	noRek = tk.Entry(inUser,textvariable=variable2, width=35).place(x=120, y=15)
	
	labelBank = tk.Label(inUser, text="Pilih Bank : ",bg='#302f2b', fg='white').place(x=15, y=50)

	kodeBank = ttk.Combobox(inUser,textvariable=variable, values=pilihanBank, width=25)
	kodeBank.place(x=120, y=50,anchor="nw")
	kirim = tk.Button(inUser, text='Kirim', command=loadingNyo, relief=tk.FLAT).place(x=345, y=50)

	win.mainloop()
