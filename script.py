import os

max_depth, in_dir, out_dir = input().split()
max_depth = int(max_depth)
print(max_depth, in_dir, out_dir)
# in_dir = '/home/daniel/testing_shell_cmds/dir1'
# max_depth = -1
#
# out_dir = '/home/daniel/testing_shell_cmds/dir2'
res_pairs = []
# print(list(os.walk(in_dir))[1])
walk_output = list(os.walk(in_dir))
for root, dirs, files in walk_output:
    s = root.removeprefix(walk_output[0][0])
    cnt_levels = len(s.split('/'))
    print(s, cnt_levels)
    if max_depth == -1 or max_depth == 1:
        for f in files:
            res_pairs.append([root + '/' + f, out_dir + '/' + f])
    else:
        for f in files:
            if cnt_levels <= max_depth:
                res_pairs.append([root + '/' + f, out_dir + s + '/' + f])
            else:
                pref = '/'.join(s.split('/')[-(max_depth - 1):])
                res_pairs.append(
                    [root + '/' + f,
                     out_dir + '/' + pref + '/' + f]
                )

names = {}


def rebuild_name(name):
    splitted = name.split('.')
    if len(splitted) >= 2:
        f, s = name.split('.')
        return f + str(names[name]) + '.' + s
    return name + str(names[name])


for i, (_, name) in enumerate(res_pairs):
    if name in names:
        res_pairs[i][1] = rebuild_name(name)
        names[name] += 1

    else:
        names[name] = 1
# print('#' * 100)
# print('Answer')
# print('#' * 100)

for x, y in res_pairs:
    print(x, y)
    # os.rename(x, y)
    try:
        os.replace(x, y)
    except:
        new_dir = '/'.join(y.split('/')[:-1])
        os.makedirs(new_dir, exist_ok=True)
        os.rename(x, y)



