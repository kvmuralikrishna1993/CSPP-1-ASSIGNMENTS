"""****************************************************"""
def payingdebtoffinayear_(bal_, annualinterst_):
    """Calculation starts here"""
    monthly_ = (annualinterst_) / 12.0
    min_ = bal_ / 12
    max_ = (bal_ * (1 + monthly_)**12) / 12.0
    unbal_ = bal_
    epsilon_ = 0.0001
    mean_ = (min_ + max_)/2
    while True:
        ti_ = 0
        while ti_ != 12:
            unbal_ = unbal_ - mean_
            unbal_ = unbal_ + (monthly_ * unbal_)
            ti_ = ti_+1
        if unbal_ > 0 and unbal_ > epsilon_:
            min_ = mean_
            unbal_ = bal_
        elif unbal_ < 0 and unbal_ < -epsilon_:
            max_ = mean_
            unbal_ = bal_
        else:
            return mean_
        mean_ = (min_ + max_)/2
def main():
    """Main function starts here"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment: " + str(round(payingdebtoffinayear_(data[0], data[1]), 2)))
if __name__ == "__main__":
    main()
