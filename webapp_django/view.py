import math
from django.http import HttpResponse
from django.shortcuts import render
import json
from pymongo import MongoClient

client = MongoClient("mongodb+srv://dbuser:dbuserdbuser@final-train-idxis.gcp.mongodb.net/test?retryWrites=true&w=majority")
#db = client.test

# try: db.command("serverStatus")
# except Exception as e: print(e)
# else: print("You are connected!")
# client.close()

db = client["dbfinal"]
collection = db["train_deleted"]

def hello(request):
    context = {}
    context['content1'] = 'Hello World!'
    return render(request, 'helloworld.html', context)


def project(request):
    result = collection.find()
    data1 = {}
    # print("start to fetch...")
    # for obj in result:
    #     if not obj['geoNetwork']['subContinent'] in data:
    #         data[obj['geoNetwork']['subContinent']] = {}
    #     if not obj['device']['deviceCategory'] in data[obj['geoNetwork']['subContinent']]:
    #         data[obj['geoNetwork']['subContinent']][obj['device']['deviceCategory']] = 0
    #     data[obj['geoNetwork']['subContinent']][obj['device']['deviceCategory']] += obj['totals']['transactionRevenue']
    # print("fetching data done...")
    data1 = {'Northern America': {'desktop': 829789150000.0,
                                  'mobile': 32529930000.0,
                                  'tablet': 5951200000.0},
             'Western Europe': {'desktop': 652440000.0, 'mobile': 0.0, 'tablet': 0.0},
             'Western Asia': {'desktop': 298090000.0, 'mobile': 0.0, 'tablet': 0.0},
             'Central America': {'desktop': 2375130000.0,
                                  'mobile': 0.0,
                                  'tablet': 41980000.0},
             'Northern Europe': {'desktop': 3263390000.0,
                                  'mobile': 2990000.0,
                                  'tablet': 0.0},
             'Southern Asia': {'mobile': 0.0,
                              'desktop': 362390000.0,
                              'tablet': 113960000.0},
             'Southeast Asia': {'mobile': 414090000.0,
                              'desktop': 2342220000.0,
                              'tablet': 0.0},
             'Eastern Europe': {'desktop': 640760000.0,
                              'mobile': 11970000.0,
                              'tablet': 0.0},
             'South America': {'desktop': 6545410000.0,
                              'mobile': 360970000.0,
                              'tablet': 382160000.0},
             'Eastern Asia': {'mobile': 129420000.0,
                              'desktop': 8205920000.0,
                              'tablet': 0.0},
             'Southern Europe': {'desktop': 585180000.0,
                                  'mobile': 43570000.0,
                                  'tablet': 0.0},
             'Australasia': {'desktop': 1957970000.0, 'mobile': 0.0, 'tablet': 0.0},
             'Central Asia': {'desktop': 0.0, 'mobile': 0.0, 'tablet': 0.0},
             '(not set)': {'desktop': 141500000.0, 'mobile': 0.0, 'tablet': 132730000.0},
             'Northern Africa': {'mobile': 0.0, 'desktop': 0.0, 'tablet': 0.0},
             'Eastern Africa': {'mobile': 0.0, 'desktop': 1999600000.0, 'tablet': 0.0},
             'Southern Africa': {'tablet': 0.0, 'desktop': 0.0, 'mobile': 0.0},
             'Western Africa': {'desktop': 1794400000.0, 'mobile': 0.0, 'tablet': 0.0},
             'Caribbean': {'mobile': 49970000.0, 'desktop': 350240000.0, 'tablet': 0.0},
             'Middle Africa': {'desktop': 0.0, 'tablet': 0.0, 'mobile': 0.0},
             'Melanesia': {'mobile': 0.0, 'desktop': 0.0, 'tablet': 0.0},
             'Micronesian Region': {'mobile': 0.0, 'desktop': 0.0, 'tablet': 0.0},
             'Polynesia': {'desktop': 0.0, 'tablet': 0.0}}
    map0 = {"Alabama":"01", "Alaska":"02" , "Arizona":"04", "Arkansas":"05", "California":"06", "Colorado":"08",
           "Connecticut":"09", "Delaware":"10", "District of Columbia":"11", "Florida":"12", "Georgia":"13",
           "Hawaii":"15", "Idaho":"16", "Illinois":"17", "Indiana":"18", "Iowa":"19", "Kansas":"20", "Kentucky":"21",
           "Louisiana":"22", "Maine":"23", "Maryland":"24", "Massachusetts":"25", "Michigan":"26", "Minnesota":"27",
           "Mississippi":"28", "Missouri":"29", "Montana":"30", "Nebraska":"31", "Nevada":"32", "New Hampshire":"33",
           "New Jersey":"34", "New Mexico":"35", "New York":"36", "North Carolina":"37", "North Dakota":"38",
           "Ohio":"39", "Oklahoma":"40", "Oregon":"41", "Pennsylvania":"42", "Rhode Island":"44", "South Carolina":"45",
           "South Dakota":"46", "Tennessee":"47", "Texas":"48", "Utah":"49", "Vermont":"50", "Virginia":"51",
           "Washington":"53", "West Virginia":"54", "Wisconsin":"55", "Wyoming":"56", "American Samoa":"60",
           "Guam":"66", "Northern Mariana Islands":"69", "Puerto Rico":"72", "U.S. Minor Outlying Islands":"74",
           "U.S. Virgin Islands":"78"}
    region_rev = {'California': 232709220000.0, 'not available in demo dataset': 340963500000.0, 'Nevada': 478600000.0,
             'Pennsylvania': 2941140000.0, 'Michigan': 15067220000.0, 'Massachusetts': 11410650000.0,
             'New York': 122146160000.0, 'Washington': 18959440000.0, 'District of Columbia': 7123940000.0,
             'Texas': 19700200000.0, 'Georgia': 6355850000.0, 'Illinois': 45984170000.0, 'Tennessee': 1562870000.0,
             '(not set)': 1490650000.0, 'Tamil Nadu': 0.0, 'Colorado': 2981840000.0, 'Virginia': 17227350000.0,
             'Quebec': 0.0, 'Santiago Metropolitan Region': 0.0, 'Wisconsin': 0.0, 'North Carolina': 1769600000.0,
             'Montana': 0.0, 'North Holland': 0.0, 'Oregon': 776260000.0, 'Taipei City': 0.0, 'England': 0.0,
             'Arizona': 1236460000.0, 'Ontario': 185690000.0, 'Seoul': 0.0, 'Ohio': 303400000.0, 'New South Wales': 0.0,
             'Minnesota': 284730000.0, 'Florida': 338660000.0, 'Delhi': 0.0, 'New Jersey': 842410000.0, 'Dubai': 0.0,
             'State of Rio de Janeiro': 50390000.0, 'Telangana': 0.0, 'County Dublin': 57570000.0,
             'Federal Territory of Kuala Lumpur': 0.0, 'Tokyo': 0.0, 'Mexico City': 0.0, 'Dnipropetrovsk Oblast': 0.0,
             'Indiana': 0.0, 'Maharashtra': 0.0, 'Makkah Province': 0.0, 'Ile-de-France': 0.0, 'Community of Madrid': 0.0,
             'Bavaria': 0.0, 'Lombardy': 0.0, 'Idaho': 0.0, 'Karnataka': 0.0, 'Zurich': 0.0, 'State of Sao Paulo': 0.0,
             'Jakarta': 0.0, 'Iowa': 96150000.0, 'Utah': 60960000.0, 'Vienna': 59990000.0, 'Oklahoma': 42960000.0,
             'Hanoi': 0.0, 'Istanbul': 0.0, 'Zhejiang': 0.0, 'Nebraska': 153450000.0, 'Maryland': 27980000.0,
             'South Carolina': 101430000.0, 'Kentucky': 0.0, 'Missouri': 65940000.0, 'Kansas': 0.0, 'Zulia': 466550000.0,
             'Uttar Pradesh': 0.0, 'Victoria': 0.0, 'Bogota': 0.0, 'Masovian Voivodeship': 0.0, 'Bangkok': 0.0,
             'New Taipei City': 0.0, 'Stockholm County': 0.0, 'Beijing': 0.0, 'Ho Chi Minh City': 0.0, 'Louisiana': 43980000.0,
             'Tel Aviv District': 0.0, 'Alabama': 0.0, 'Hawaii': 0.0, 'Buenos Aires': 0.0, 'Lesser Poland Voivodeship': 0.0,
             'Berlin': 0.0, 'Baja California': 0.0, 'State of Minas Gerais': 0.0, 'British Columbia': 0.0, 'Catalonia': 32280000.0,
             'Prague': 0.0, 'Riyadh Province': 0.0, 'Metro Manila': 0.0, 'Alberta': 0.0, 'Hamburg': 0.0, 'Hesse': 0.0,
             'Queensland': 0.0, 'Dublin City': 0.0, 'Moscow': 0.0, 'Haryana': 0.0, 'Quintana Roo': 0.0, 'Bucharest': 0.0}
    data2 = {}
    for i in region_rev.keys():
        if i in map0.keys():
            if region_rev[i] != 0:
                data2[map0[i]] = math.log(region_rev[i])
            else:
                data2[map0[i]] = 0

    medium_rev = {'referral': 23675780000.0, 'organic': 146362340000.0, '(none)': 679913100000.0, 'cpc': 20713880000.0,
                  'cpm': 30758660000.0, 'sites.google.com': 2151050000.0, 'google': 165200650000.0,
                  '(direct)': 679913100000.0, 'analytics.google.com': 9490000.0, 'Partners': 44970000.0, 'google.com': 396940000.0,
                  'bing': 2242690000.0, 'youtube.com': 249330000.0, 'quora.com': 25980000.0, 'info.com': 1,
                  'l.facebook.com': 413210000.0, 'groups.google.com': 1000840000.0, 'docs.google.com': 731480000.0,
                  'm.facebook.com': 88870000.0, 'yahoo': 674260000.0, 'mail.google.com': 12694800000.0, 'm.youtube.com': 39470000.0,
                  'ask': 3960000.0, 'pinterest.com': 95960000.0, 'dfa': 29713320000.0, 'hangouts.google.com': 414700000.0,
                  'dealspotr.com': 2121520000.0, 'reddit.com': 7970000.0, 'phandroid.com': 69430000.0, 'facebook.com': 595210000.0, 'support.google.com': 147130000.0,
                  'connect.googleforwork.com': 111980000.0, 't.co': 166920000.0, 'duckduckgo.com': 129040000.0, 'affiliate': 44970000.0,
                  'plus.google.com': 134360000.0, 'keep.google.com': 44790000.0, 'away.vk.com': 54610000.0, 'l.messenger.com': 15190000.0,
                  'search.xfinity.com': 56480000.0, 'mail.aol.com': 56850000.0, 'chat.google.com': 1523520000.0,
                  'mg.mail.yahoo.com': 79970000.0, 'trainup.withgoogle.com': 18990000.0, 'my.yahoo.com': 29700000.0, 'start.wow.com': 1,
                  'ex.fit.edu': 1, 'searchlock.com': 1, 'bing.com': 1, 'google.sk': 1, 'mail.yahoo.com': 1, 'google.be': 1,
                  'google.com.bd': 1, 'search.myway.com': 1, 'google.gr': 1, 'ausdroid.net': 1, 'kidrex.org': 1,
                  'images.google.com': 1, 'marketingland.com': 1, 'myaccount.google.com': 1, 'newclasses.nyu.edu': 1,
                  'gatewaycdi.com': 1, 'google.com.hk': 1, 'm.sp.sm.cn': 1, 'm.yz.sm.cn': 1, 'vk.com': 1
                  }
    data3 = medium_rev
    return render(request, 'projects.html', {'data1': json.dumps(data1), 'data2': json.dumps(data2),
                                             'map0': json.dumps(map0), 'data3': json.dumps(data3)})

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def models(request):
    return render(request, 'services.html')


def linear_regression(request):
    return render(request, 'linear_regression.html')


def random_forest(request):
    return render(request, 'random_forest.html')


def lightGBM(request):
    return render(request, 'lightGBM.html')


def gradient_boosting(request):
    return render(request, 'gradient_boosting.html')


def nn(request):
    return render(request, 'nn.html')


def cnn(request):
    return render(request, 'cnn.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')
