from django import forms

class SearchForm(forms.Form):
    choice = (("AED","AED"),("AFN","AFN"),("ALL","ALL"),("AMD","AMD"),("ANG","ANG"),("AOA","AOA"),("ARS","ARS"),("AUD","AUD"),("AWG","AWG"),("AZN","AZN"),("BAM","BAM"),("BBD","BBD"),("BDT","BDT"),("BGN","BGN"),("BHD","BHD"),("BIF","BIF"),("BMD","BMD"),("BND","BND"),("BOB","BOB"),("BRL","BRL"),("BSD","BSD"),("BTN","BTN"),("BWP","BWP"),("BYN","BYN"),("BZD","BZD"),("CAD","CAD"),("CDF","CDF"),("CHF","CHF"),("CLP","CLP"),("CNY","CNY"),("COP","COP"),("CRC","CRC"),("CUC","CUC"),("CUP","CUP"),("CVE","CVE"),("CZK","CZK"),("DJF","DJF"),("DKK","DKK"),("DOP","DOP"),("DZD","DZD"),("EGP","EGP"),("ERN","ERN"),("ETB","ETB"),("EUR","EUR"),("FJD","FJD"),("GBP","GBP"),("GEL","GEL"),("GHS","GHS"),("GIP","GIP"),("GMD","GMD"),("GNF","GNF"),("GTQ","GTQ"),("GYD","GYD"),("HKD","HKD"),("HNL","HNL"),("HRK","HRK"),("HTG","HTG"),("HUF","HUF"),("IDR","IDR"),("ILS","ILS"),("INR","INR"),("IQD","IQD"),("IRR","IRR"),("ISK","ISK"),("JMD","JMD"),("JOD","JOD"),("JPY","JPY"),("KES","KES"),("KGS","KGS"),
    ("KHR","KHR"),("KMF","KMF"),("KPW","KPW"),("KRW","KRW"),("KWD","KWD"),("KYD","KYD"),("KZT","KZT"),("LAK","LAK"),("LBP","LBP"),("LKR","LKR"),("LRD","LRD"),("LSL","LSL"),("LYD","LYD"),("MAD","MAD"),("MDL","MDL"),("MGA","MGA"),("MKD","MKD"),("MMK","MMK"),("MNT","MNT"),("MOP","MOP"),("MRO","MRO"),("MUR","MUR"),("MVR","MVR"),("MWK","MWK"),("MXN","MXN"),("MYR","MYR"),("MZN","MZN"),("NAD","NAD"),("NGN","NGN"),("NIO","NIO"),("NOK","NOK"),("NPR","NPR"),("NZD","NZD"),("OMR","OMR"),("PAB","PAB"),("PEN","PEN"),("PGK","PGK"),("PHP","PHP"),("PKR","PKR"),("PLN","PLN"),("PYG","PYG"),("QAR","QAR"),("RON","RON"),("RSD","RSD"),("RUB","RUB"),("RWF","RWF"),("SAR","SAR"),("SBD","SBD"),("SCR","SCR"),("SDG","SDG"),("SEK","SEK"),("SGD","SGD"),("SHP","SHP"),("SLL","SLL"),("SOS","SOS"),("SRD","SRD"),("STD","STD"),("SYP","SYP"),("SZL","SZL"),("THB","THB"),("TJS","TJS"),("TMT","TMT"),("TND","TND"),("TOP","TOP"),("TRY","TRY"),("TTD","TTD"),("TWD","TWD"),("TZS","TZS"),("UAH","UAH"),("UGX","UGX"),("USD","USD"),("UYU","UYU"),("UZS","UZS"),("VND","VND"),("VUV","VUV"),("WST","WST"),("XAF","XAF"),("XCD","XCD"),("XOF","XOF"),("XPF","XPF"),("YER","YER"),("ZAR","ZAR"),("ZMW","ZMW"),)    
    departure = forms.CharField(max_length=255)
    destination = forms.CharField(max_length=255)
    departure_date = forms.CharField(max_length=10)
    arrival_date = forms.CharField(max_length=10, required=False)
    currency = forms.ChoiceField(choices=choice)
