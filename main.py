from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler, ConversationHandler, MessageHandler,Filters
import test_base
import base

API_TOKEN = '2140701433:AAHOLhTkb0ffH8olHpwIHVU0YUQFWmED8nc'
global OCHQ_TESTLAR


ADMIN = 1
USER = 2
QABUL_ADMIN = 3
EDIT = 4
EDITED = 5
OCHISH = 6
VIEW_NAT = 7
VIEW_ISM = 8
VIEW_VARIANT = 9
TESTGA_QATNASHISH = 10


def start(update, context):
	btns_admin = ReplyKeyboardMarkup(
		[
			['📝 Test Yaratish'],['📈 Natijalar'],['✏️ Testlarni boshqarish']
		], resize_keyboard=True)
	btns_user = ReplyKeyboardMarkup(
		[
			['📈 Natijalar'],
			['📋 Testga qatnashish']
		], resize_keyboard=True)
	global admin_1, admin_2, admin_3
	admin_1 = "Abduqodir_GQ"
	admin_2 = "Fayziyev_UM"
	admin_3 = "Ulugbek_MF"
	global u
	u = update.effective_user.username
	
	if u==admin_1 or u==admin_2 or u==admin_3:
		update.message.reply_html(f"Assalomu aleykum <b>{update.effective_user.first_name}</b> ✋\nNima qilishni quyidagi tugmalardan tanlang 👇", reply_markup=btns_admin)
		return ADMIN
	else:
		update.message.reply_html(f'Assalomu aleykum <b>{update.effective_user.first_name}</b> ✋', reply_markup=btns_user)

		return USER

def test_yaratish(update, context):

	update.message.reply_html(f'  Test yaratish uchun\n<b>🔢 Variant kodi</b>\n<b>🎯 To\'g\'ri javoblarni</b>\nquyidagi tartibda yuboring\n<b>Variant kodi/To\'g\'ri javoblar</b>\n\nGQQ/abcddcba...aaadd\n	yoki\nGQQ/1a2b3c4d5d6c7b...')
	return QABUL_ADMIN

def admin_natijalar(update, context):
	nat_in_btn = [
		[
			InlineKeyboardButton('🔸 Ism familiya', callback_data='ism'),
			InlineKeyboardButton('🔹 Variant', callback_data='variant'),
		],
		[
			InlineKeyboardButton('🔙 Orqaga', callback_data='orqaga'),
		]
	]
	update.message.reply_html(f'Natijalarni qaysi shaklda ko\'rmoqchisiz ⁉️. Quyidagi tugmalardan tanlang 👇', reply_markup=InlineKeyboardMarkup(nat_in_btn))
	return VIEW_NAT


# Admindan kelgan malumotlarni split qiladi va bazaga saqlaydi
def qabul_admin(update, context):
	txt = update.message.text
	arr = list(map(str, txt.split('/')))
	if len(arr)==2:
		if test_base.variant_conf(arr[0]):
			s = ""
			m_base = ''
			i = 0
			if arr[1][0]!='1':
				for item in arr[1]:
					i+=1
					s += f"<b>{i}. </b> {item}\n"
					m_base += item
				test_base.test_ochish(arr[0], m_base)
			elif len(arr[1])<=18:
				if len(arr[1])%2==0 :
					t = 0
					while i<len(arr[1])/2:
						i+=1
						s += f"<b>{i}. </b> {arr[1][t]}\n"
						m_base += arr[1][t]
						t+=2
					test_base.test_ochish(arr[0], m_base)
				else:
					update.message.reply_html(f'Ma\'lumotlarni ko\'rsatilgan tartibda kiriting 👆')
					return QABUL_ADMIN
			elif (len(arr[1])-18)%3==0:
				t = 1
				while i<9:
					i+=1
					s += f"<b>{i}.   </b> {arr[1][t]}\n"
					m_base += arr[1][t]
					t+=2
				l = 0
				t=20
				while l<(len(arr[1])-18)/3:
					i+=1
					l+=1
					s += f"<b>{i}.  </b> {arr[1][t]}\n"
					m_base += arr[1][t]
					t+=3
				test_base.test_ochish(arr[0], m_base)
			else:
				update.message.reply_html(f'Ma\'lumotlarni ko\'rsatilgan tartibda kiriting ⌨️ yoki kiritilgan ma\'lumotni tekshirib ko\'ring 👆')
				return QABUL_ADMIN
				
			update.message.reply_html(f'Variant - <b>{arr[0]}</b>\n{s}\n\nTest yaratildi 👌. Testni boshlash uchun \n<b>"✏️ Testlarni boshqarish"</b> ni bosing')
			return ADMIN
		else:
			update.message.reply_html(f'Siz yaratgan <b>Variant kodi</b> oldindan mavjud. Iltimos Variantni boshqacha kodlab keyin jo\'nating 📲')
			return QABUL_ADMIN
	else:
		update.message.reply_html(f'Ma\'lumotlarni ko\'rsatilgan tartibda kiriting ⌨️')
		return QABUL_ADMIN
def test_edit(update, context):
	edit_btn = [
		[
		InlineKeyboardButton('📭 Ochish', callback_data='ochish'),
		InlineKeyboardButton('📫 Yopish', callback_data='yopish'),
		],
		[InlineKeyboardButton('🔙 Orqaga', callback_data='orqaga'),]
	]
	update.message.reply_html(f'Testlarni nazorat qilish uchun quyidagi tugmalardan tanlang 👇', reply_markup=InlineKeyboardMarkup(edit_btn))
	return EDIT

def edit(update, context):
	query = update.callback_query
	txt = query.data
	query.message.delete()
	
	if txt == 'orqaga':
		query.message.reply_html(f"Nima qilishni quyidagi tugmalardan tanlang 👇")
		return ADMIN
	elif txt == 'ochish':
		query.message.reply_html(f"Ochmoqchi bo'lgan testingiz varianti kodini yuboring 📲")
		return OCHISH
	else:
		query.message.reply_html(f"Yopmoqchi bo'lgan testingiz varianti kodini yuboring 📲")
		return EDITED
def edited(update, context):
	txt = update.message.text
	m = test_base.test_holati(txt)
	if m=='yopiq':
		update.message.reply_html(f'{txt} - variantli test yopiq 🚫')
	else:
		t = test_base.test_yopish(txt)
		update.message.reply_html(t)
	return ADMIN
def ochish(update, context):
	txt = update.message.text
	m = test_base.test_holati(txt)
	if m=='ochiq':
		update.message.reply_html(f'{txt} - variantli test ochiq ☑️')
	else:
		t = test_base.test_yopish(txt)
		update.message.reply_html(t)
	return ADMIN


def view_nat(update, context):
	query = update.callback_query
	txt = query.data
	
	if txt=='ism':
		query.message.reply_html(f"Natijasini bilmoqchi bo'lgan <b>Ism Familiya</b>ni yuboring 📲")
		return VIEW_ISM
	elif txt=='variant':
		query.message.reply_html(f"Natijasini bilmoqchi bo'lgan <b>Variant Kodi</b>ni yuboring 📲")
		return VIEW_VARIANT
	else:
		query.message.reply_html(f"Nima qilishni quyidagi tugmalardan tanlang 👇")
		t = update.effective_user.username
		if u==admin_1 or u==admin_2 or u==admin_3:
			return ADMIN
		else:
			return USER

def view_ism(update, context):
	txt = update.message.text
	t = base.ism_view(txt)
	info = f"<b>{txt}</b> natijalari\n<b>№</b>\t |  <b>Variant</b>  \t|<b> To\'g\'ri javob</b>\t| <b>Sana</b>\n"
	if len(t)>0:
		i=0
		for item in t:
			i+=1
			info += f"{i}.\t {item[1]} \t|  {item[2]} ta  \t|  {item[4]}\n"
	else:
		info = f"Kechirasiz <b>{txt}</b> - variantiga oid ma\'lumot topilmadi 🤷🏻‍♂️"
	update.message.reply_html(info)
	if u==admin_1 or u==admin_2 or u==admin_3:
		return ADMIN
	else:
		return USER


def view_variant(update, context):
	txt = update.message.text	
	t = base.variant_view(txt) 
	info = f"Variant - <b>{txt}</b> natijalari\n<b>№</b>\t |  <b>F.I.O</b>     \t|<b>To\'g\'ri javob</b>\t| <b>Sana</b>\n"
	if len(t)>0:
		i=0
		for item in t:
			i+=1
			info += f"{i}.\t {item[0]} \t|  {item[2]} ta  \t|  {item[4]}\n"
	else:
		info = f"Kechirasiz <b>{txt}</b> - variantiga oid ma\'lumot topilmadi 🤷🏻‍♂️"
	update.message.reply_html(info)
	if u==admin_1 or u==admin_2 or u==admin_3:
		return ADMIN
	else:
		return USER

# Userlar natijalar bilan tanishishi uchun
def user_test(update, context):
	update.message.reply_html(f'Testga qatnashish uchun\n<b>Variant kodi</b>\n<b>Javoblar</b>\n<b>Ism Familiya</b>ni quyidagi tartibda yuboring\nVariant kodi/Javoblar/Ism Familiya\nGQQ/abcddcba...aaadd/G\'aniyev Qodirjon\nyoki\nGQQ/1a2b3c4d5d6c7b.../G\'aniyev Qodirjon')
	return TESTGA_QATNASHISH

def testga_qatnashish(update, context):
	txt = update.message.text
	arr = list(map(str, txt.split('/')))
	x = test_base.test_topshirish(arr[0])
	if len(arr)!=3:
		update.message.reply_html(f'Ma\'lumotlarni ko\'rsatilgan tartibda kiriting 👆')
		return TESTGA_QATNASHISH
	if test_base.var_tek(arr[0]):
		update.message.reply_html(f' <b>{arr[0]}</b> - varianti bo\'yicha ma\'lumot topilmadi 🤷🏻‍♂️. Iltimos variantni tekshiring 🔍')
		return USER

	if test_base.test_holati_user(arr[0]):
		update.message.reply_html(f'🚷 <b>{arr[0]}</b> - varianti bo\'yicha testga qatnashishga ruxsat yo\'q')
		return USER


	if base.ismni_tek(arr[2], arr[0]):
		update.message.reply_html(f"Siz bu testga oldin qatnashgansiz 🧐. Har bir variant bo\'yicha bir marta qatnashish mumkin 👮🏿‍♀️.")
		return USER

	if type(x)==tuple:
		m_base = ''
		i = 0
		if True:
			if (test_base.variant_conf(arr[0])):
				
				if arr[1][0]!='1':
					for item in arr[1]:
						i+=1
						m_base += item
				elif len(arr[1])<=18:
					if len(arr[1])%2==0 :
						t = 0
						while i<len(arr[1])/2:
							i+=1
							m_base += arr[1][t]
							t+=2
					else:
						update.message.reply_html(f'Ma\'lumotlarni ko\'rsatilgan tartibda kiriting 👆')
						return TESTGA_QATNASHISH
				elif (len(arr[1])-18)%3==0:
					t = 1
					while i<9:
						i+=1
						m_base += arr[1][t]
						t+=2
					l = 0
					t=20
					while l<(len(arr[1])-18)/3:
						i+=1
						l+=1
						m_base += arr[1][t]
						t+=3
			
			else:
				update.message.reply_html(f'Siz kiritgan <b>{arr[0]}</b> - Variant kodi mavjud emas. Iltimos Variant kodini tekshirib keyin jo\'nating 📲')
				return TESTGA_QATNASHISH

			if len(m_base)==len(x[1]):
				c = 0
				t_j=0
				l = []
				for item in x[1]:
					if item==m_base[c]:
						t_j += 1
					else:
						tl = f"{c+1}.    {m_base[c]}    |  {item}\n"
						l.append(tl)
					c+=1
				xato = ""
				if len(l)!=0:
					xato = "№   ❌   |   ✅\n"
					for it in l:
						xato+= it
				else:
					xato = "Xatolar yo'q"
				foiz = (t_j/len(x[1]))*100
				sana = test_base.vaqt
				q = (f"{arr[2]}", f"{arr[0]}", f"{t_j}", f"{foiz}", f"{sana}")
				base.qaydnoma(q)
				update.message.reply_html(f'<i>Tabriklaymiz</i> <b>{arr[2]}</b>\nSiz ushbu testda quyidagi natijani qayd etdingiz\n🎯 To\'g\'ri javoblar:  <b>{t_j}</b> ta\nXatolar:\n{xato}\nFoiz ko\'rsatkichi: {foiz} %\n\nUmumiy natijalarni ko\rish uchun "📈 Natijalar"ga murojaat qiling')
			else:
				update.message.reply_html(f'Ma\'lumotlarni ko\'rsatilgan tartibda kiriting yoki kiritilgan ma\'lumotni tekshirib ko\'ring 👆')
				return TESTGA_QATNASHISH
			return USER
	else:
		update.message.reply_html(f'Ma\'lumotlarni ko\'rsatilgan tartibda kiriting 👆')
		return TESTGA_QATNASHISH
	return USER
	
				


def main():
	updater = Updater(API_TOKEN, use_context=True)

	dispatcher = updater.dispatcher
	conv_handler = ConversationHandler(
		entry_points = [CommandHandler('start', start)],

		states = {
			ADMIN: [
				MessageHandler(Filters.regex('^📝 Test Yaratish$'), test_yaratish ),
				MessageHandler(Filters.regex('^📈 Natijalar$'), admin_natijalar ),
				MessageHandler(Filters.regex('^✏️ Testlarni boshqarish$'), test_edit ),
			],
			USER: [
				MessageHandler(Filters.regex('^📈 Natijalar$'), admin_natijalar),
				MessageHandler(Filters.regex('^📋 Testga qatnashish$'), user_test),
			],
			QABUL_ADMIN: [
				MessageHandler(Filters.text, qabul_admin)
			],
			EDIT: [CallbackQueryHandler(edit)],
			EDITED: [MessageHandler(Filters.text, edited)],
			OCHISH: [MessageHandler(Filters.text, ochish)],
			VIEW_NAT: [CallbackQueryHandler(view_nat)],
			VIEW_ISM: [MessageHandler(Filters.text, view_ism)],
			VIEW_VARIANT: [MessageHandler(Filters.text, view_variant)],       
			TESTGA_QATNASHISH: [MessageHandler(Filters.text, testga_qatnashish)],

		},
		fallbacks = [CommandHandler('help', help)]
	)

	dispatcher.add_handler(conv_handler)
	updater.start_polling()
	updater.idle()

main()