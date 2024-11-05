ItemsInChart = 0

#if ItemsInChart != 2:
    #raise Exception("Product Count does not match!")

if ItemsInChart != 2: #do nothing
    pass

assert(ItemsInChart == 0)

#try, catch
try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)

finally:
    print("Cleaning up resources")