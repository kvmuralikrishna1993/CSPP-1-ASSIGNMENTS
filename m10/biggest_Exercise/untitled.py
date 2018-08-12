def funk():
	num_ = input()
    adict_ = {}
    for i in range(int(num_)):
        set_ = input()
        mset_ = set_.split()
        if mset_[0][0] not in adict_:
            adict_[mset_[0][0]] = [mset_[1]]
        else:
            adict_[mset_[0][0]].append(mset_[1])
    print(adict_)