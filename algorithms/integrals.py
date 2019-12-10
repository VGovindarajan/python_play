import math
def sine_values():
    splitter = 100000
    #print("Sine 45 = {0}".format(math.sin(45)))
    sum = 0.0
    count = 0
    for i in range (1,  314159, 1):
        sine_input = i/splitter
        sine_value = math.sin(sine_input)
        #print("Sine {0} = {1}".format(sine_input,sine_value ))
        if sine_value > 0:
            sum += (sine_value*(1/splitter))
            count +=1
    Average = (sum/count)*splitter
    print("Count = {0}, Calculated Sum = {1}, Calculated Average = {2}".format(sum))
    print("Count = {0}".format(count))
    print("Average = {0}".format(Average))
    cos_pi = math.cos(22.0/7.0)
    cos_zero = math.cos(0)
    integral_sum = -cos_pi + cos_zero
    integral_average = integral_sum/((22/7)-0)
    print("Using Fundamental Theorem of Calculus, cos_pi={0}, cos_zero={1}, integral_Sum={2}, integral_average={3}".format(cos_pi, cos_zero, integral_sum, integral_average))

def main():
    sine_values()

if __name__ == "__main__":
    main()