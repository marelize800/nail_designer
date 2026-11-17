import streamlit as st
import random as r





nail_shapes = [
    "Square",
    "Almond",
    "Lipstick",
    "Round",
    "Oval",
    "Sqoval",
    "Soft Square",
    "Russian Almond",
    "Coffin",
    "Stiletto"
]

colors = [
    "#FDF5E6", "#FAF0E6", "#F5F5DC", "#FAFAD2", "#FFF8DC",
    "#F5DEB3", "#FFE4C4", "#FFDEAD", "#F4EBE1", "#E8D3C3",
    "#DEB887", "#D2B48C", "#C4A482", "#BC8F8F", "#D8B4A0",
    "#C19A6B", "#B69B84", "#A67B5B", "#8C6239", "#FFDAB9",
    "#FFCBC4", "#F9D5C5", "#E8C3B9", "#DDA79A", "#C99385",
    "#B57F73", "#E0A99D", "#F2CC8F", "#E7BC91", "#B38B6D",
    "#A38068", "#94725C", "#82634E", "#705340", "#C2B280",
    "#B3A17B", "#9E8B69", "#8A7959", "#76664A", "#63553C",
    "#B8A293", "#A48F82", "#917C71", "#7D6960", "#6A574E",
    "#EAD9CD", "#D9C3B0", "#C8AC95", "#B7967A", "#A6805F"
]

bases = ["#345123",
"#488337",
"#257910",
"#318203",
"#933124",
"#397459",
"#855742",
"#571676",
"#442928",
"#117969",
"#920963",
"#443330",
"#275774",
"#966933",
"#682000",
"#376579",
"#491240",
"#489858",
"#288163",
"#622521",
"#603010",
"#743283",
"#102892",
"#521728",
"#557818",
"#450198",
"#155350",
"#234410",
"#297960",
"#992524",
"#827459",
"#705956",
"#705840",
"#83168",
"#743870",
"#192719",
"#643228",
"#375746",
"#909853",
"#496046",
"#368515",
"#585140",
"#447089",
"#591618",
"#716510",
"#916495",
"#11036",
"#879323",
"#82242",
"#765069",
"#456780",
"#840829",
"#586641",
"#856815",
"#111921",
"#947502",
"#591782",
"#978743",
"#305554",
"#867607",
"#414416",
"#971169",
"#677789",
"#955248",
"#874323",
"#646670",
"#312143",
"#136729",
"#416649",
"#523027",
"#908456",
"#103589",
"#397415",
"#459374",
"#112413",
"#771197",
"#928354",
"#111625",
"#778047",
"#981280",
"#318981",
"#553774",
"#485031",
"#159191",
"#205262",
"#477777",
"#669081",
"#349192",
"#303324",
"#172124",
"#712112",
"#325652",
"#509256",
"#286676",
"#402409",
"#266221",
"#776807",
"#958497",
"#925174",
"#417799",
"#238441",
"#258857",
"#383699",
"#347905",
"#395568",
"#741852",
"#822413",
"#754869",
"#200746",
"#531884",
"#322627",
"#347268",
"#574627",
"#134918",
"#141112",
"#156529",
"#618269",
"#245055",
"#999981",
"#484067",
"#899592",
"#347322",
"#709455",
"#865345",
"#678805",
"#651916",
"#105229",
"#103190",
"#926915",
"#499003",
"#991303",
"#851278",
"#212763",
"#971511",
"#486980",
"#915047",
"#147461",
"#538039",
"#187635",
"#385073",
"#230397",
"#161701",
"#159271",
"#304051",
"#178766",
"#735126",
"#478128"
]

designs = ['French tips','chrome','cateye','3D shapes','ombre','abstract','handpainted','chunky']
lengths = ['short','medium','long','extra long','extremely long']


pick_shape = r.choice(nail_shapes)
pick_nude = r.choice(colors)
pick_base = r.choice(bases)
pick_des = r.choice(designs)
pick_len = r.choice(lengths)

st.title('Your simple Nail Designer!')
st.text('Generate a color,style,base color, and design with one click!')
st.divider()


# c1,c2 = st.columns(2)

# with c1:
# 	st.subheader('Primary Color')
# 	with st.container(key='base_color'):
# 		st.text('Primary Color')

# with c2:
# 	st.subheader('Base Color')
# 	with st.container(key='nude_color'):
# 		st.text('Base Color')

with st.container(border=False):
	if st.button('Generate my desing'):
		c1,c2 = st.columns(2)
		with c1:
			st.subheader('Primary Color')
			with st.container(key='base_color'):
				st.text('Primary Color')

		with c2:
			st.subheader('Base Color')
			with st.container(key='nude_color'):
				st.text('Base Color')

		st.subheader('Nail Shape')
		if pick_shape == "Square":
			st.image('images/square.png',width=150)
		if pick_shape == "Almond":
			st.image('images/almond.png',width=150)
		if pick_shape == "Lipstick":
			st.image('images/lipstick.png',width=150)
		if pick_shape == "Round":
			st.image('images/round.png',width=150)
		if pick_shape == "Oval":
			st.image('images/oval.png',width=150)
		if pick_shape == "Sqoval":
			st.image('images/sqoval.png',width=150)
		if pick_shape == "Soft Square":
			st.image('images/soft_square.png',width=150)
		if pick_shape == "Russian Almond":
			st.image('images/russian_almond.png',width=150)
		if pick_shape == "Coffin":
			st.image('images/coffin.png',width=150)
		if pick_shape == "Stiletto":
			st.image('images/stiletto.png',width=150)

st.html(f"""
<style>
.st-key-base_color{{
	border-radius: 999px;
	background-color: {pick_base};
	min-width: 100px;
	min-height: 50px;
	display:flex;
	flex-direction:row;
	justify-content:center;
	align-items:center
	}}
.st-key-nude_color{{
	border-radius: 999px;
	background-color: {pick_nude};
	min-width: 100px;
	min-height: 50px;
	display:flex;
	flex-direction:row;
	justify-content:center;
	align-items:center
	}}
</style>
	""")
