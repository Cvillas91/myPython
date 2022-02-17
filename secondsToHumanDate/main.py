import string


def format_duration(seconds):
    string_final = ""
    res =["","","","","",""]
    dict = {"years":0,"days":0,"hours":0,"minutes":0,"seconds":0}
    count = 0

    if seconds == 0:
        return "now"
        exit()

    if seconds/31536000 >= 1 :
        dict["years"] = seconds // 31536000
        seconds = seconds - dict["years"] * 31536000
        res[0] = "1 year" if dict["years"] == 1 else str(dict["years"]) + " years"
        count +=1
    
    if seconds/86400 >= 1 :
        dict["days"] = seconds // 86400
        seconds = seconds - dict["days"] * 86400
        res[1] = "1 day" if dict["days"] == 1 else str(dict["days"]) + " days"
        count +=1

    if seconds/3600 >= 1 :
        dict["hours"] = seconds // 3600
        seconds = seconds - dict["hours"] * 3600 
        res[2] = "1 hour" if dict["hours"] == 1 else str(dict["hours"]) + " hours"
        count +=1

    if seconds/60 >= 1 :
        dict["minutes"] = seconds // 60
        seconds = seconds - dict["minutes"] * 60
        res[3] = "1 minute" if dict["minutes"] == 1 else str(dict["minutes"]) + " minutes"
        count +=1
    
    if seconds != 0 :
        dict["seconds"] = seconds
        res[4] = "1 second" if dict["seconds"] == 1 else str(dict["seconds"]) + " seconds"
        count +=1
    
    for i in range(5) :
        if res[i] != "" and i != 5:
            string_final += res[i] + ", "

    string_final = string_final[:-2]
    if count > 1:
        string_final = string_final[:string_final.rfind(",")] + " and" + string_final[string_final.rfind(",") + 1:]

    return string_final

print(format_duration(60))

