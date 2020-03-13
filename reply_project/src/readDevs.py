def read_devs(devs):
    developer_list = []
    for developer in devs:
        developer_skill_list = []
        descriptions = developer.split(' ')
        descriptions.pop(2) # remove number of skills
        for description in range(2, len(descriptions)):
            developer_skill_list.append(descriptions[description])
        descriptions2 = []
        descriptions2.append(descriptions[0])
        descriptions2.append(descriptions[1])
        descriptions2.append(developer_skill_list)
        developer_list.append(descriptions2)
    return developer_list
