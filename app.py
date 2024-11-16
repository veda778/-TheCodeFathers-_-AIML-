from flask import Flask, render_template, request, redirect, url_for
import requests
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        job_role = request.form.get("job_role")
        location = request.form.get("location")
        result = naukri(job_role, location)
        # You can process these inputs here or pass them to another function.
        print(f"Job Role: {job_role}, Location: {location}")
        #return result
        
        # Redirect to a results page or render a response.
        return render_template("results.html",result = result, job_role=job_role, location=location)
    return render_template("input.html")

#@app.route("/results")
#def results():
 #   return "<h1>Results Page</h1>"

def naukri(job_title, location):
    


    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'appid': '109',
        'clientid': 'd3skt0p',
        'content-type': 'application/json',
        # 'cookie': 'test=naukri.com; _t_s=direct; _t_r=1030%2F%2F; persona=default; _t_ds=77b55a31731667762-38477b55a3-077b55a3; J=0; _ga=GA1.1.1623646606.1731667766; _gcl_au=1.1.1790328039.1731667772; _t_us=67382CA4; bm_mi=EAC4F6D807127395E8F0D0C9808C7CE1~YAAQFtcLF8HyNCWTAQAAH6FxMxmn6xBkKobQZnxnfjmGYX2YZO7lizCoLcXu8O5hQa738RU3ulHjehf62l7DD7eAEmOD+lKiJ+o2jBb/t7uhaoi9WX1Mm8SuF/jhank31jyNymDLSoXUnJIrDe5g/IinhLCfgBYMcMhBUTu3h1WAVSiF/pdIqievdif3FAGhRUJQusvXjzvoZLHb0WirYmXK8pbl7Jsi8XGz5+R8kh0iuTGpa6vmYPoqtCOlXF+5SP0VAqs2Hk9zUjXaSa1mo/Ka82tCAYdAlRnugLxd9V6kLlfK3EYyMHq57+S5JkGvT+ye6MwgButAfeDQPXinGv9nriRpuji5XZRyneptA+f7mNjbm8J0~1; _ga_T749QGK6MQ=GS1.1.1731734693.2.1.1731734905.0.0.0; ak_bmsc=052C41C0F7B17FE4EB239389B0FFA216~000000000000000000000000000000~YAAQFtcLF9zyNCWTAQAAO6RxMxlANq/K26cGV/MnSojIx9BypHiF6B5gii1Qm8LZ9lIhz9AfjN8CEEIw++nItMGATP4fU19DbSr+KyZmaAec5J1YP5vZdtCOeHtn4h3/L0A+rvSIZxZ6Crmz3MyQrcgH3kcdBBqxKT8QnlMI+AfqmnKscERKOhN1RcZSn63HAfvQctcrn47NJZEzKc9k9EIAFhad3bRJxRaZ0+k+nuZcRmqw/Pwr4aVyYLWumpSlFne2wLMEstNqd0xgGKvknuZPeULbMRjK/kdRKMaMJw/I15DmtH9qCQXVaiIp6wLTFkZNWkJs+b+ag1VhDqSKFFTxq0GItPKyWQG+7QkSDyAqOWP6X7mNkpKJqImEY+xLTOXN1o55pXiBVfxBeBXpZyGxQHegwLRM+R0YLaUvay/Z/h1Nf/ZI1/extncv7ZDbyiGl9Wx2/bQgBG+5o9wisgi1AAkRf9QkJna9EysebUJu9KVOJlSu3KJRNgFyihpbyQS21WI1pmBg5NsIuFMaBXsyMufjZM4gQQ==; __gads=ID=1d627a12d01406d5:T=1731667800:RT=1731734906:S=ALNI_MZpMn_84QsCUa2Fggcm41BX0PZiuQ; __gpi=UID=00000f69dd28ecf5:T=1731667800:RT=1731734906:S=ALNI_MZXUEdHkgPlhG_NI2eR_YFGFWTA2g; __eoi=ID=0d675a5225f934cb:T=1731667800:RT=1731734906:S=AA-AfjYhbj6gRoaAWL1X5qytQeSJ; bm_sv=6546623CC3D031D1DBA4F6AFC357FE5E~YAAQFtcLF7H0NCWTAQAA+FlyMxmWJHNnAFhFKv05eCzvxdDyGF05RUH7idV6/yFtDuuD292D86XcsCVZKbIbavzhcHpEhvBdIvLuJIR5UZCctHUnkbx8/mxRhiGwa3zxoziL9Tdr8/2xa9t8LZq+hk0QyxaNXFcU5FH8z/Xin9HY9e99jcGDOinPWj74KDKip24zgrHZjaGtM5qF40bY71HrSfdXwX+JqeGsp0/nHBwcCbjdycovVCXF4227CS8j6Q==~1; HOWTORT=ul=1731734952293&r=https%3A%2F%2Fwww.naukri.com%2Ffullstack-web-developer-jobs-in-bengaluru%3Fk%3Dfullstack%2520web%2520developer%26l%3Dbengaluru%26experience%3D0&hd=1731734952422; _ga_K2YBNZVRLL=GS1.1.1731734006.2.1.1731734952.13.0.0',
        'gid': 'LOCATION,INDUSTRY,EDUCATION,FAREA_ROLE',
        #'nkparam': 'rXt6I5Z6rhlPJc+D7oALUslv7E/MR/BTnQ25gdnFxba/fi7pIV9t8zyHfas6NP84imJjrxqRH8k6Vtd+pKQmdA==',
        'priority': 'u=1, i',
        #'referer': 'https://www.naukri.com/fullstack-web-developer-jobs-in-bengaluru?k=fullstack%20web%20developer&l=bengaluru&experience=0',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'systemid': 'Naukri',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }
    
    params = [
        ('noOfResults', '20'),
        ('urlType', 'search_by_key_loc'),
        ('searchType', 'adv'),
        ('location', location),
        ('keyword', job_title),
        ('pageNo', '1'),
        ('experience', '0'),
        ('k', job_title),
        ('l', location),
        ('experience', '0'),
        #('seoKey', 'fullstack-web-developer-jobs-in-bengaluru'),
        ('src', 'jobsearchDesk'),
        ('latLong', ''),
    ]
    
    response = requests.get('https://www.naukri.com/jobapi/v3/search', params=params, headers=headers)
    print(response.json())
   
    return response.json()['jobDetails']

if __name__ == "__main__":
    app.run(debug=True)
