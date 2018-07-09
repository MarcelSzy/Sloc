import math
#dif != 0, rat != 1 && rat > 0
def cal(dif, rat, d):
	tel_p = float(dif/abs(rat-1))
	tel_l = float(tel_p*rat)
	k_tel_p = 0
	k_tel_l = 0
	if tel_l>tel_p:
		if ((math.pow(d,2)+math.pow(tel_p,2)) > math.pow(tel_l,2)):
			c = (math.pow(tel_l,2)-math.pow(tel_p,2)-math.pow(d,2))/(2*d)
			h = math.pow(tel_p,2)-math.pow(c,2)
			h = math.sqrt(abs(h))
			k_tel_l = math.asin(math.sin(h/tel_l))
			k_tel_p = math.asin(math.sin(h/tel_p))
		if ((math.pow(d,2)+math.pow(tel_p,2)) == math.pow(tel_l,2)):
			h=tel_p
			k_tel_l = math.asin(math.sin(h/tel_l))
			k_tel_p = math.pi/3
		if ((math.pow(d,2)+math.pow(tel_p,2)) < math.pow(tel_l,2)):
			c = (-1*math.pow(tel_l,2)+math.pow(tel_p,2)+math.pow(d,2))/(2*d)
			h = math.pow(tel_p,2)-math.pow(c,2)
			h = math.sqrt(abs(h))
			k_tel_l = math.asin(math.sin(h/tel_l))
			k_tel_p = math.asin(math.sin(h/tel_p))

	if tel_l<tel_p:
		if ((math.pow(d,2)+math.pow(tel_l,2)) < math.pow(tel_p,2)):
			c = (-1*math.pow(tel_p,2)+math.pow(tel_l,2)+math.pow(d,2))/(2*d)
			h = math.pow(tel_l,2)-math.pow(c,2)
			h = math.sqrt(abs(h))
			k_tel_l = math.asin(math.sin(h/tel_l))
			k_tel_p = math.asin(math.sin(h/tel_p))
		if ((math.pow(d,2)+math.pow(tel_l,2)) == math.pow(tel_p,2)):
			k_tel_l = math.pi/3
			h=tel_l
			k_tel_p = math.asin(math.sin(h/tel_p))
		if ((math.pow(d,2)+math.pow(tel_l,2)) > math.pow(tel_p,2)):
			c = (math.pow(tel_p,2)-math.pow(tel_l,2)-math.pow(d,2))/(2*d)
			h = math.pow(tel_l,2)-math.pow(c,2)
			h = math.sqrt(abs(h))
			k_tel_p = math.asin(math.sin(h/tel_p))
			k_tel_l = math.asin(math.sin(h/tel_l))
	return tel_l, tel_p, math.degrees(k_tel_l), math.degrees(k_tel_p)


