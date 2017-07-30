from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from forms import KillForm, KillFormText
import models
from django.http import JsonResponse


# Create your views here.


def home(request, pagenum=0):
    pagenum = int(pagenum)
    step = 10
    total = models.Kill.objects.all().count()
    lower = min(pagenum * step, total)
    upper = min((pagenum + 1) * step, total)
    kills = models.Kill.objects.all().order_by("date")[lower:upper]
    return render(request, "main.html", {"kills": kills.reverse(), "page": pagenum})


def postkill(request):
    form = KillFormText()
    if request.method == "GET":
        return render(request, "killform.html", {"formset": form})
    elif request.method == 'POST':
        d = request.POST
        try:
            saveData(d)
        except:
            return JsonResponse({"Success":False})
        return JsonResponse({"Success": True})
    return render(request, "killform.html", {"formset": form})


def saveData(d):
    kill = models.Kill()
    victimPlayer = {}
    maxAttackers = 0
    for key in d:
        if "Attacker " in key:
            getNum = int(key.replace("Attacker ", "").split("[")[0])
            if getNum > maxAttackers:
                maxAttackers = getNum
    attackers = [{} for x in xrange(maxAttackers)]
    print attackers

    for key in d:
        print key, d[key]
        if "Date" in key:
            kill.date = d[key]

        if "Zone" in key:
            zone, success = models.Zone.objects.get_or_create(name=d[key])
            zone.save()
            kill.zone = zone

        if "Victim" in key:
            if "Agent" in key:
                victimPlayer["Agent"] = d[key]
            if "Corp" in key:
                victimPlayer["Corp"] = d[key]
            if "Robot" in key:
                victimPlayer["Robot"] = d[key]

        elif "Attacker " in key:
            getNum = int(key.replace("Attacker ", "").split("[")[0]) - 1
            if "Agent" in key:
                attackers[getNum]["Agent"] = d[key]
            if "Corp" in key:
                attackers[getNum]["Corp"] = d[key]
            if "Robot" in key:
                attackers[getNum]["Robot"] = d[key]
            if "Damage" in key:
                attackers[getNum]["Damage"] = d[key]
            if "ECM" in key:
                attackers[getNum]["ECM"] = d[key]
            if "Demob" in key:
                attackers[getNum]["Demob"] = d[key]
            if "Sensor" in key:
                attackers[getNum]["Sensor"] = d[key]
            if "Energy" in key:
                attackers[getNum]["Energy"] = d[key]

    print "-------------"
    print attackers
    print "--------------"

    attackDetailSet = set()
    for attacker in attackers:
        corp, success = models.Corp.objects.get_or_create(name=attacker["Corp"])
        corp.save()
        agent, success = models.Player.objects.get_or_create(name=attacker["Agent"], corp=corp)
        agent.save()
        robot, success = models.Robot.objects.get_or_create(name=attacker["Robot"])
        robot.save()

        ecmSplit = attacker["ECM"].split("/")
        dmgNum = attacker["Damage"].split(" HP")[0]
        attackDetails, success = models.AttackDetails.objects.get_or_create(player=agent, robot=robot, damage=dmgNum,
                                                                            killing_blow=False,
                                                                            ecm_hits=ecmSplit[0],
                                                                            ecm_attempts=ecmSplit[1],
                                                                            demob=attacker["Demob"],
                                                                            suppress=attacker["Sensor"],
                                                                            energy=attacker["Energy"])

        attackDetails.save()
        attackDetailSet.add(attackDetails)
    agent = []
    corp = []
    robot = []
    corp, success = models.Corp.objects.get_or_create(name=victimPlayer["Corp"])
    corp.save()
    agent, success = models.Player.objects.get_or_create(name=victimPlayer["Agent"], corp=corp)
    agent.save()
    robot, success = models.Robot.objects.get_or_create(name=victimPlayer["Robot"])
    robot.save()

    kill, success = models.Kill.objects.get_or_create(date=kill.date, zone=kill.zone, victim_agent=agent,
                                                      victim_robot=robot)
    kill.attackers.add(*attackDetailSet)
    kill.save()


def printdata(data):
    print data


def walkDict(d, func):
    for key in d:
        if type(d[key]) is dict:
            walkDict(d[key], func)
        else:
            func(key)
            func(d[key])
