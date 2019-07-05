import operator

def graph_barons_kills(matches):
    list_barron = []
    baron_kills = matches.find({},{"teams.baronKills":1, "_id":0})
    count_matches = matches.count_documents({})
    res_sum = 0
    for r in range(count_matches) :
        for i in range(1):
            list_barron.append(baron_kills[r]['teams'][i]['baronKills'])
    return list_barron

def winner(key, matches):
    t=[]
    win = 0 
    cursor = matches.find({},{"teams.teamId":1,"teams.win":1, "_id":0})
    l = [r for r in cursor]
    for x in range(len(l)):
        for y in range(2):
            if l[x]['teams'][y]['teamId'] == key:
                if l[x]['teams'][y]['win'] == "Win":
                    win = 1
                else:
                    win = 0
    return win


def sum_kill(key, matches):
    t=[]
    sum = 0
    cursor = matches.find({},{"participants.teamId":1,"participants.stats.kills":1, "_id":0})
    l = [r for r in cursor]
    
    for x in range(len(l)):
        for y in range(10):
            if l[x]['participants'][y]['teamId'] == key:
                sum+=(l[x]['participants'][y]['stats']['kills'])
               
    return sum / len(l)

def most_used_items(matches,items):
    match_items = matches.find({},{
        "participants.stats.item0":1,
        "participants.stats.item1":1,
        "participants.stats.item2":1,
        "participants.stats.item3":1,
        "participants.stats.item4":1,
        "participants.stats.item5":1,
        "participants.stats.item6":1
    })
    item_ids_total = []
    for i in range(match_items.count()):
        for j in range(6):
            last_index = 'item'+(str(j+1))
            for k in range(10):
                item_id = match_items[i]['participants'][k]['stats'][last_index]
                item_ids_total.append(item_id)

    dictItems = {k:item_ids_total.count(k) for k in set(item_ids_total)}
    dict_items_sorted = dict(reversed(sorted(dictItems.items(), key=operator.itemgetter(1))))

    item_ids = []
    i = 0
    for x in dict_items_sorted:
        if i > 10:
            break
        item_ids.append(x)
        i = i + 1

    item_ids.remove(0)
    l = item_ids
    itemNames = []
    for i in l:
        itemName = items.find({},{"data."+str(i)+".name":1})
        itemNames.append(itemName[0]['data'][str(i)]['name'])
    return itemNames

def most_used_masteries(matches,masteries):
    matches_masteries = matches.find({},{"participants.masteries.masteryId":1})
    mastery_ids_total = []
    for i in range(matches_masteries.count()):
        for k in range(9):
            for x in matches_masteries[i]['participants'][k]['masteries']:
                mastery_ids_total.append(x['masteryId'])
    dict_masteries = {str(k):mastery_ids_total.count(k) for k in set(mastery_ids_total)}
    dict_masteries_sorted = dict(reversed(sorted(dict_masteries.items(), key=operator.itemgetter(1))))
    mastery_ids = []
    i = 0
    for x in dict_masteries_sorted:
        if i > 10:
            break
        mastery_ids.append(x)
        i = i + 1

    h = mastery_ids
    mastery_names = []
    for i in h:
        mastery_name = masteries.find({},{"data."+str(i)+".name":1})
        mastery_names.append(mastery_name[0]['data'][str(i)]['name'])
    return mastery_names

def average_wards_placed(matches):
    average_wards_placed = matches.find({},{"participants.stats.wardsPlaced":1,  "_id":0})
    count_matches = matches.count_documents({})
    sums = 0
    for r in range(count_matches) :
        for i in range(10):
            sums = sums + (average_wards_placed[r]['participants'][i]['stats']['wardsPlaced'])
    return sums / count_matches / 10

def average_total_damage_dealt(matches):
    avg_tot_dmg_dealt = matches.find({},{"participants.stats.totalDamageDealt":1,  "_id":0})
    count_matches = matches.count_documents({})
    sums = 0
    for r in range(count_matches) :
        for i in range(10):
            sums = sums + (avg_tot_dmg_dealt[r]['participants'][i]['stats']['totalDamageDealt'])

    return sums / count_matches / 10

def average_largest_killing_spree(matches):
    avg_lgst_kill_spree = matches.find({},{"participants.stats.largestKillingSpree":1,  "_id":0})
    count_matches = matches.count_documents({})
    sums = 0
    for r in range(count_matches) :
        for i in range(10):
            sums = sums + (avg_lgst_kill_spree[r]['participants'][i]['stats']['largestKillingSpree'])
    return sums / count_matches / 10


def average_total_heal(matches):
    avg_tot_heal = matches.find({},{"participants.stats.totalHeal":1,  "_id":0})
    count_matches = matches.count_documents({})
    sums = 0
    for r in range(count_matches) :
        for i in range(10):
            sums = sums + (avg_tot_heal[r]['participants'][i]['stats']['totalHeal'])

    return sums / count_matches / 10


def average_total_minions_killed(matches):
    avg_tot_min_kills = matches.find({},{"participants.stats.totalMinionsKilled":1,  "_id":0})
    count_matches = matches.count_documents({})
    sums = 0
    for r in range(count_matches) :
        for i in range(10):
            sums = sums + (avg_tot_min_kills[r]['participants'][i]['stats']['totalMinionsKilled'])
    return sums / count_matches / 10


def avg_earned_gold(key, matches):

    t=[]
    sum = 0
    cursor = matches.find({},{"participants.teamId":1,"participants.stats.goldEarned":1, "_id":0})
    l = [r for r in cursor]
    for x in range(100) :
        for y in range(10):
            if l[x]['participants'][y]['teamId'] == key:
                sum += (l[x]['participants'][y]['stats']['goldEarned'])
    
    avg = sum / 100
    return avg


def avg_spent_gold(key, matches):    
    t=[]
    sum = 0
    cursor = matches.find({},{"participants.teamId":1,"participants.stats.goldSpent":1, "_id":0})
    l = [r for r in cursor]
    for x in range(len(l)) :
        for y in range(10):
            if l[x]['participants'][y]['teamId'] == key:
                sum+=(l[x]['participants'][y]['stats']['goldSpent'])
    avg = sum/100    
    return avg


def avg_true_Damage(key, matches):
    
    t=[]
    sum = 0
    cursor = matches.find({},{"participants.teamId":1,"participants.stats.trueDamageDealt":1, "_id":0})
    l = [r for r in cursor]
    for x in range(len(l)):
        for y in range(10):
            if l[x]['participants'][y]['teamId'] == key:
                sum+=(l[x]['participants'][y]['stats']['trueDamageDealt'])
    avg = sum/len(l)   
    return avg


def sum_kill_win(matches):
    if winner(100, matches) == 1:
        return sum_kill(100, matches)
    else:
        return sum_kill(200, matches)


def sum_kill_lost(matches):
    if winner(100, matches) == 0:
          return sum_kill(100, matches)
    else:
        return sum_kill(200, matches)


def blue_team_first_blood(matches):
    cursor = matches.count_documents(
    {"teams.0.firstBlood":True})
    return(cursor)


def red_team_first_blood(matches):
    cursor2 = matches.count_documents(
    {"teams.1.firstBlood":True})
    return(cursor2)


def avg_baron_kills(matches):
    baron_kills = matches.find({},{"teams.baronKills":1, "_id":0})
    count_matches = matches.count_documents({})
    res_sum = 0
    for r in range(count_matches) :
        for i in range(1):
            res_sum = res_sum + (baron_kills[r]['teams'][i]['baronKills'])
        
    avg = res_sum/count_matches
    pourcentage = int(avg * 100)
    return str(pourcentage) + "%"


def sum_minions_killed(matches):
    sum_killed_minions = matches.find({},{"participants.stats.totalMinionsKilled":1,  "_id":0})
    count_matches = matches.count_documents({})
    res_sum = 0
    for r in range(count_matches) :
        for i in range(10):
            res_sum = res_sum + (sum_killed_minions[r]['participants'][i]['stats']['totalMinionsKilled'])
    return res_sum


def avg_living_time(matches):
    avg_time_living = matches.find({},{"participants.stats.longestTimeSpentLiving":1,  "_id":0})
    count_matches = matches.count_documents({})
    res_sum = 0
    for r in range(count_matches) :
        for i in range(10):
            res_sum = res_sum + (avg_time_living[r]['participants'][i]['stats']['longestTimeSpentLiving'])

    return ((res_sum/(count_matches * 10))/60)