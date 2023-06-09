from time import perf_counter
import matplotlib.pyplot as plt

def shortest_common_supersequence(s1, s2, memo={}):
    # Si los resultados ya están almacenados en la matriz, los devolvemos
    if (s1, s2) in memo:
        return memo[(s1, s2)]
    
    # Caso base: si una de las cadenas está vacía, la otra es la supersecuencia más corta
    if len(s1) == 0:
        memo[(s1, s2)] = s2
        return s2
    elif len(s2) == 0:
        memo[(s1, s2)] = s1
        return s1
    
    # Si los últimos caracteres de ambas cadenas son iguales, podemos agregar uno solo de ellos
    if s1[-1] == s2[-1]:
        result = shortest_common_supersequence(s1[:-1], s2[:-1], memo) + s1[-1]
        memo[(s1, s2)] = result
        return result
    
    # De lo contrario, debemos agregar el último carácter de cada cadena y encontrar la supersecuencia más corta entre las dos opciones
    s1_left = shortest_common_supersequence(s1[:-1], s2, memo) + s1[-1]
    s2_left = shortest_common_supersequence(s1, s2[:-1], memo) + s2[-1]
    if len(s1_left) < len(s2_left):
        result = s1_left
    else:
        result = s2_left

    memo[(s1, s2)] = result
    return result

def get_graph():
    sequencias = [["ABCDE", "FGHIJ"], ["KLMNOPQRSTU", "VWXYZABCDEFGHIJKLMNO"], ["PQRSTUVWXYZABCDEFGHIJKLMNO", "PQRSTUVWXYZABCDEFGHIJKLMNO"], ["LMNOPQRSTUVWXYZABCDEFGHIJ", "LMNOPQRSTUVWXYZABCDEFGHIJ"]]
    sequencias = [["ABCD", "ACDF"],["ABDDF", "ACDFE"],["ABCDDF", "UCDFER"],["ABCDDFR", "ACDFERW"],["TWABCDDF", "ABCDDFRT"],["RETFASDFA", "ABCDDFRDL"],["PVYZASDVCU", "GTVRJBDGNT"]]
    sequencias = [['OTNYQWIEXHZ', 'HYYLQCH'], ['VXTPAKLG', 'KYQKFEYTMVIPZOHXIYTB'], ['TDK', 'GYWYX'], ['NUYPDE', 'HSIBFTTYEEEBOZGLSIP'], ['YOTOINNDSFCTHFYRA', 'RPTHBTDFDIDIMDP'], ['CUKCIDCAIFUU', 'AKJOMWVNC'], ['WTCGBVCBEAPPF', 'PSDRPERDLXWCEZ'], ['P', 'LAGEAIQJ'], ['ICLDHFKZWGX', 'CSQSXYBBOVCEYPJW'], ['SJNFKYREKMAPJWXIG', 'UWEBGEVCMYVDTTHYKCM']]
    sequencias = [['NOWFYNGHEQ', 'LPDRPLHLOS'], ['TVMZAHTCWWRQSLMJXICT', 'RXQUMCRKIZONNDSADWTF'], ['NSBQWZNLJBTXDRHGERHRDTNQSHKQIZ', 'QBUJVFAPCMTGVJERFAXJUCDZHTIDGA'], ['NFBPEHHFTHOTSXUUHWUDGAQFWAFDEFFGBKPDFLSN', 'HYJAGZMUYXHQLUNQZOHFOQTZUZNGMGWQIMDMTKII'], ['LPRFXJNIUZELIWURKFJZODJZNCRTVYUBCKQKNOZDRIUTCFRUTN', 'IVGJJFEIHDCILFOPGOPYCLDAQDSNHERZRDCYJYEGYGJKUFJXCV'], ['UVVRIUMKJXFZWNXCAHHNHXSIUNCGHRHXBVKKDSEJSTNNQNNIKGUVJRXQMBZN', 'YZHMHBIVHQCHZZEZCOMKZRZMOZFJSOIDMBKFOOMZSSXQKDHUDQALPIRRTAJV'], ['QUPTOUSQRALJDJWXITJSHGCCOBCVPNKMFHZOYQNMBYMEPADVCTRJTLIRJGQGJYNXVTSTJX', 'UTSJUJRLPTSPBGZGQMRIIKUSPEVSKKCDWZYBNLUQZSGIVDLOOCAUJRPRZFRWMIVRQYLONJ'], ['WWRZVYUBQGWFDAAWTUZPVHEQKFEFADBLSNZPNGUNQCTUOULLLVJJRCJZOBPIFHXNAPJOCPHDFTPEJPVL', 'CQUUVGBPSBHJVSNBWUBBNETJPLZDOYVJZSKPDEQANZQJJDAJUPTEWKSCCQHSUOXPJHXXLLEBPHQAKRUR'], ['IWIZEKDLAHEHZLEMOBJLVDVNYHGXPVEACCZZBFCDUOUPHCUDIHGEABMYIWXDPKADTSWWFNZGLGECOTCTRYMGKPAXTG', 'VXQJRTUUAYXXUGJIHLDVJEATXVSUTLDXLQMEWZKWPIRBFAAKEOZHAAXOBEJONVYHWZCXCCFQTOAQONTSYTHZMCEEGV'], ['OLFEGHXVSCHLAEVNAAEIDQSQHHNKHFQIKWZHXWJVCIWZEQKVWUWPMEEHJAIJTICNVQICSHAFUVKJCVYYJXHWZLDQEDWOPCEPEMGB', 'PTESCVOQWPTMTLZTKMMVUOWRAJFPAQHYSKJIBRWPBYZOXOTYOURRHVRQOPLLUNNGFYRFPGVBSOZRCBVHZNIWELONZYRMKGXLJWMT'], ['PUHEBVSJVYUPJLQOWCQPQKRPOUBWSXQVOEKEIZJZLBHRAJCGRCPROEWHXGQCTPRPVACAHFCVHLWXLVADSWNMJUFOAARTOWBKVFURIQXQDTCTUU', 'LEWUMLYTRWNRYUPTNDKCODCSFNPWUNCNFVEVBPKGKAFJSCOTCLBTSIKYQAJHLVWUGVPCKXZLMOVIAVTARIITPDDDIBQSFAJLHBWMLENFPFWRYN'], ['FWLMHZBZGRGJAVZKGIDFKGTZAFSYRZGRKRFEGHLJECLWRLEEHGTFKLQEOHFHMVGKIEVQSYEKJUJQJGIUXBYTPOXHPOCNXVWFORAFGMVSXMZJAOJRPRDVGGLP', 'KCXFSHXUOZCMTCQYCQQCWRBCKFCKLVFDGJJJXZJABFGLRZNGTGXGMZMAUPVLYXJNFCTRVSFJIYEFKVFGHHSALGMQYRVSUWFYKNEWVMCBOENOCHAPHDBZSJOJ'], ['KIFFNRULEZXENRTBHWHIWWGOTZHIZYXBYYUKCLIVZTIVCGSPCKPGDOOIFCKJRFSEJVXECJCSPBGAFTMSAFRMBGQLKKSBGMLFBNSORSDAUDALSAWWWTSPKEMYQHOONBJKVL', 'WWZMVGANNPXORHAHEFLYGJHCYKFGJRTXPJNOBMGFGKXFWLDFAATLRZTITRSWEVFOFOXNLMLSQLKZHXTVKZTTHRCWYCQJWPPDFQVSTRPYFNFGDTCVYZTQUDGLLAUEOJWKBE'], ['DHNGWEAWXIYPOKLJVAVIYJGMDWBDPNOJXXRSDZNKAHKYVPGVCDCHRVKIDGIDBLNMRSWOYLNSTJUHKYIOJQQYGVPZBGFDBTKMJKDHZMRRDOAQRYWJSXOGFZHLUBHNCCRVRPIRJXONWKYD', 'DRSXTDDJWLBKYQWUAWZFJHTURWTWLGHHASBJZZCKGPEOJUSQISZKOATZWWDPLTVWXHKDRCKKUCCBIBMPYDDRRMJKHLPQUJDOMDEOHAGUQCGWAKDVICNDSSXFSEKKPJEVXJQTWZWQVJBQ'], ['TWRWQRZHQSSYLIYIWKCNLUVZHWNVSIVPJTTMARAQXIXLACBUBMZBJZCTFNADKTLTEEGMZOCVUXFYVOAOJFFEZOZMUXPSEKQBOWYNOOIPEORHPLEXSTIBKONSXTPBTACWBRXLEXBONEJAHISIIBTUJA', 'UKAIJYWLNXNIUTQGUZILULKQFOJYUCVRVGJONHTBICBEAMETDAMBWIXHTRFPLKTLKJXYZOQBEEOLPJIVJUNQWXTREIFNZVSUZGSBQVPMLEASDPAOLGNHYLUQOGNVJHURPGUZDUZLMVCICFMLLMQUZR'], ['OVITIGEFWAIMRVNSDTHGZOPUORLZHAQZFKCVMKZTKDJNGBEMIBDXAKYWQPEBWMKZECUWXLZIFUFTGGLDOFRVJCOCVAMKSDFZETURFBXYKLMXMKMJTREWCFMPHWSYCRBVPEKVGZTRFDSYZAIZRRAOHZTUOHTCBILN', 'OYOVLJSTJGCVJTNLNHKGYOWWVDSBXLJVUKKWTERHMLRKYDADQNLHYWVOAUJEVKLANRDJIKISJYSTJYSDMRGIBQPZXNWKUTBSSKDIYBLTZCJALOOKCHJAKHFAKUZWQBECTVQKKZIUNLEMCVWCBQXQUOJTUPWMFLJK'], ['MIVAJEBHHSFKYAUYOSKCDDECRYRPRQYGCJBXEBJSAIWVJDQFDNZYADUHLUBBFKUOWYDKJLELEKBTWQHEMEFZIJCGAUHIKLLOHPOJCBGISYUPFJVLKYNNHFINZXTKLXUUKXCINGFCQIXNMUESRIDNRPWYQKAVVRGUDJLTEWHCVL', 'VASNIMFKNGPSLDKJDYSZATRQTIVXMORGMBYTVEBWOWGCQJRVMFLDHIQTBQOYXQCCLGOPYLFXLYYUPHTCMHNHPALHLSTZTMSLEPTXQPWNKWZOWMRGTQAELRWSRKDYQNAXUVEXZXOTHRVLZNEGGJYMMYTQJDGRZWALMAHHIQCXAY'], ['HDUCRXKWZUVXYEZKFTAEAHTIJNCSDISXLYNZWHZSWTNZZESPKTXZVHZVIIQTDLQAJZKBXCMUBRISOGIXKPCBVMXJQMNAVUKFJRBHBERBUOFPDABVOXOVPUQEOBGKZMOSKVMBKMMGTZIMBQYKGFRWZKQTUGJRYGJULTZXGWAYSKRDJBAOMRSK', 'UMPAXCMUPAEZFIYROLTLPUHOCATGQZGCOGKFIMUMQCPOENAEYPCMKXSIGODGYHEZBTWULWXRVZYQVLULORAOBXOHSATHRGQYTUBUNFGQYLVWGLNZZLDPLSTDEUHSOJHAHDQJTRBKZAHVHPQLNKZHMWWYJEBWRCACBQXSLHXCWWGBJOVBTYRO'], ['HGKVTSMBAZCOZQIFCQQXVALQRFGQYNJPVABVZIDLBNTNBPGIAONIORXWTSKTFXCXZGZAWHEWTROXHUVEIDWQUAYHEYJCDWRXDWCTYAZAZFUIUYJJDCXVHXXRGAYKTCYBDTVIWELGFPPZKZWBBHAXKXAVVOLQMYIGEOYNJDNBTTZBCCRJPCDPVYGWEAPQDR', 'QCHOEOMKWKNMAPWFHRPRGCJDCYZMWMPARKCAPEVWUHQSVCCONOFNGVZVGMZTRTMWIPNNJJSHAAAOGKTUVKMWNSWJBSTXEBDUVHMAZLCJXZNJXRFYMOGOVVQSVSUZBWPMKWKIXBXHSVKGADLWLMWMFRQOBJIVXSAEBQCVLFXKJWJYXUSKEFDTBZKKJCLCFO'], ['XMIUWOFPMQETQUMJUPMYZJLXRPPSEIBNPZEPDLRGJCZEVHXCQJQZOARMMKNXNYWHYWUHJDBHPPTFZLCINHKKTYGCXZVKWHPNDPVRKYFJYWAJOFTYKVQZZVEWGRMYZAWIOITOZAFRKHWJKDAANMGCDALARUVIIBZPNDVECZDAKXRBXBSKVSTQHPVPEYSIYANFAJGPARMC', 'UTCIEKEIANAVUZUSMEDEGCYONKULIPLJTSSPJMSTXINRQDFTKTHFBKCEOSLOMVXEWPVNNDQYPXOGAPRXMGFSWFHNIZREFPIPRWEVDVMUDFKBPOJJNEFVLFGOVZOBLLVYKGJDEHEAOUYUIOJPNSGYKHZFFZBKREXDLMKKJOXARCTGPFGWYTFPNBOFOTMSUUWDGIJBUQDH']]
    resultados = []
    tiempos = []

    for i in range(1, len(sequencias)):
        start = perf_counter()
        res = shortest_common_supersequence(sequencias[i][0], sequencias[i][1])
        end = perf_counter()
        resultados.append(len(res))
        tiempos.append(end - start)

    # plot resultados contra tiempos
    plt.plot(resultados, tiempos)
    # plt.plot(range(1, len(sequencias)), tiempos)
    plt.show()
    


