import re

def main(event):
  
  pName = event.get("inputFields").get("plan_name")
  
  if "hrs" in pName:
    match = re.search(r'\d+-hrs', pName)
    hour = match.group(0)
    hours = int(hour.split("-")[0])
  else:
    hours = 0
    
  return {
    "outputFields": {
      "PlanName": pName,
      "hours": hours
    }
  }