#This dictionary contains all compound forms recognized as such from SAA1+ (via hyphens)
from spacy.lang.tokenizer_exceptions import BASE_EXCEPTIONS
from spacy.symbols import ORTH, NORM, LEMMA
from spacy.util import update_exc

exclusions = [

{
   "ša-rēšīya":[{ORTH:    "ša-rēšīya"}],
   "ša-rēšāni":[{ORTH:    "ša-rēšāni"}],
   "ša-rēšīšu":[{ORTH:    "ša-rēšīšu"}],
   "ša-rēši":[{ORTH:    "ša-rēši"}],
   "ša-qurbūtu":[{ORTH:    "ša-qurbūtu"}],
   "ša-qurbūti":[{ORTH:    "ša-qurbūti"}],
   "ša-qurbūte":[{ORTH:    "ša-qurbūte"}],
   "ša-bēti-šanie":[{ORTH:    "ša-bēti-šanie"}],
   "šalše-ūme":[{ORTH:    "šalše-ūme"}],
   "šalši-ūme":[{ORTH:    "šalši-ūme"}],
   "šalši-ūmēšu":[{ORTH:    "šalši-ūmēšu"}],
   "ša-muhhi-āli":[{ORTH:    "ša-muhhi-āli"}],
   "ša-muhhi-bēti":[{ORTH:    "ša-muhhi-bēti"}],
   "ša-muhhi-bētāni":[{ORTH:    "ša-muhhi-bētāni"}],
   "ša-pān-ēkalli":[{ORTH:    "ša-pān-ēkalli"}],
   "ša-maṣṣarti":[{ORTH:    "ša-maṣṣarti"}],
   "ša-pēthallāte":[{ORTH:    "ša-pēthallāte"}],
   "ša-pēthallāti":[{ORTH:    "ša-pēthallāti"}],
   "ša-pēthal":[{ORTH:    "ša-pēthal"}],
   "ša-bēti-šanie":[{ORTH:    "ša-bēti-šanie"}],
   "ša-bēti-šaniūte":[{ORTH:    "ša-bēti-šaniūte"}],
   "ša-sāgātēšu":[{ORTH:    "ša-sāgātēšu"}],
   "ṣalmāt qaqqadi":[{ORTH:    "ṣalmāt qaqqadi"}],
   "māt Aššur":[{ORTH:    "māt Aššur"}],
   "māt tāmti":[{ORTH:    "māt tāmti"}],
   "māt tāmtimuwa":[{ORTH:    "māt tāmtimuwa"}],
   "māt tāmtimma":[{ORTH:    "māt tāmtimma"}],
   "bēl šemērē":[{ORTH:    "bēl šemērē"}],
   "bēl ṭēmīya":[{ORTH:    "bēl ṭēmīya"}],
   "bēl ṣīlti":[{ORTH:    "bēl ṣīlti"}],
   "bēl adê":[{ORTH:    "bēl adê"}],
   "bēl bēlē":[{ORTH:    "bēl bēlē"}],
   "bēl ṣāssīya":[{ORTH:    "bēl ṣāssīya"}],
   "bēl dabāba":[{ORTH:    "bēl dabāba"}],
   "bēlē dabāba":[{ORTH:    "bēlē dabāba"}],
   "bēl dabābīya":[{ORTH:    "bēl dabābīya"}],
   "bēl dāmī": [{ORTH: "bēl dāmī"}],
   "bēl dāmē":[{ORTH:    "bēl dāmē"}],
   "bēl dāmēya":[{ORTH:    "bēl dāmēya"}],
   "bēl dāmēkunu":[{ORTH:    "bēl dāmēkunu"}],
   "bēl dāmēšunu":[{ORTH:    "bēl dāmēšunu"}],
   "bēl qiʾʾi":[{ORTH:    "bēl qiʾʾi"}],
   "bēl hiṭṭi":[{ORTH:    "bēl hiṭṭi"}],
   "bēl harrānīšu":[{ORTH:    "bēl harrānīšu"}],
   "bēl nakar":[{ORTH:    "bēl nakar"}],
   "bēl nakri":[{ORTH:    "bēl nakri"}],
   "bēl nakrīšu":[{ORTH:    "bēl nakrīšu"}],
   "bēl nakrīya":[{ORTH:    "bēl nakrīya"}],
   "bēl hiṭṭīya":[{ORTH:    "bēl hiṭṭīya"}],
   "bēl hīṭu":[{ORTH:    "bēl hīṭu"}],
   "bēl hīṭi":[{ORTH:    "bēl hīṭi"}],
   "bēl mugerri":[{ORTH:    "bēl mugerri"}],
   "bēl mugerrī":[{ORTH:    "bēl mugerrī"}],
   "bēl mugirri":[{ORTH:    "bēl mugirri"}],
   "bēl mugirrī":[{ORTH:    "bēl mugirrī"}],
   "bēl nakrīka":[{ORTH:    "bēl nakrīka"}],
   "bēl sīhi":[{ORTH:    "bēl sīhi"}],
   "bēl salāmīšu":[{ORTH:    "bēl salāmīšu"}],
   "bēl salāmīni":[{ORTH:    "bēl salāmīni"}],
   "bēl ṣāssi":[{ORTH:    "bēl ṣāssi"}],
   "bēl habulli":[{ORTH:    "bēl habulli"}],
   "bēl ṣāssīšunu":[{ORTH:    "bēl ṣāssīšunu"}],
   "bēl habullīšunu":[{ORTH:    "bēl habullīšunu"}],
   "bēl pīhāti":[{ORTH:    "bēl pīhāti"}],
   "bēl piqittēma":[{ORTH:    "bēl piqittēma"}],
   "bēl piqitte":[{ORTH:    "bēl piqitte"}],
   "bēl piqitti":[{ORTH:    "bēl piqitti"}],
   "bēl piqittāti":[{ORTH:    "bēl piqittāti"}],
   "bēl piqittīya":[{ORTH:    "bēl piqittīya"}],
   "bēl piqittēya":[{ORTH:    "bēl piqittēya"}],
   "bēl piqittāte":[{ORTH:    "bēl piqittāte"}],
   "bēl qātātišunu":[{ORTH:    "bēl qātātišunu"}],
   "bēl ālāni":[{ORTH:    "bēl ālāni"}],
   "bēl ālūtê":[{ORTH:    "bēl ālūtê"}],
   "bēl āli":[{ORTH:    "bēl āli"}],
   "bēl dīnu":[{ORTH:    "bēl dīnu"}],
   "bēl dēnīšu":[{ORTH:    "bēl dēnīšu"}],
   "bēl dīnīya":[{ORTH:    "bēl dīnīya"}],
   "bēl ṭābtūtīni":[{ORTH:    "bēl ṭābtūtīni"}],
   "bēl ṭābātekunu":[{ORTH:    "bēl ṭābātekunu"}],
   "bēl ṣāltīya": [{ORTH: "bēl ṣāltīya"}],
   "bēl ṣēlti": [{ORTH: "bēl ṣēlti"}],
   "bēl ṭābātīšu":[{ORTH:    "bēl ṭābātīšu"}],
   "bēl ṭābtišunu":[{ORTH:    "bēl ṭābtišunu"}],
   "bēl ṭābti":[{ORTH:    "bēl ṭābti"}],
   "bēl ṭābtīya":[{ORTH:    "bēl ṭābtīya"}],
   "bēl tahūmešunu":[{ORTH:    "bēl tahūmešunu"}],
   "bēlē ṭābtēya":[{ORTH:    "bēlē ṭābtēya"}],
   "bēlē ṭābti":[{ORTH:    "bēlē ṭābti"}],
   "bēl ṭābtī":[{ORTH:    "bēl ṭābtī"}],
   "bēlē ṭābtī":[{ORTH:    "bēlē ṭābtī"}],
   "bēlē hīṭu":[{ORTH:    "bēlē hīṭu"}],
   "arû šūluk":[{ORTH:    "arû šūluk"}],
   "ummi šarri":[{ORTH:    "ummi šarri"}],
   "ummi abīšu":[{ORTH:    "ummi abīšu"}],
   "šamnu ṭābu":[{ORTH:    "šamnu ṭābu"}],
   "ṣīt libbīya":[{ORTH:    "ṣīt libbīya"}],
   "ṣīt Šamaš":[{ORTH:    "ṣīt Šamaš"}],
   "mazzāz pāni":[{ORTH:    "mazzāz pāni"}],
   "ēkal māšarti":[{ORTH:    "ēkal māšarti"}],
   "ēkal māšarte":[{ORTH:    "ēkal māšarte"}],
   "manzāz ēkalli": [{ORTH: "manzāz ēkalli"}],
   "kal ūme": [{ORTH: "kal ūme"}],
   "rab şibti": [{ORTH: "rab şibti"}],
   "rab maddaʾti": [{ORTH: "rab maddaʾti"}],
   "rab daria": [{ORTH: "rab daria"}],
   "rab širakī": [{ORTH: "rab širakī"}],
   "rab rēʾî": [{ORTH: "rab rēʾî"}],
   "rab qalti": [{ORTH: "rab qalti"}],
   "rab qašti": [{ORTH: "rab qašti"}],
   "rab bīrāti": [{ORTH: "rab bīrāti"}],
   "rab bīti": [{ORTH: "rab bīti"}],
   "rab abullāti": [{ORTH: "rab abullāti"}],
   "rab ēkalli": [{ORTH: "rab ēkalli"}],
   "rab pilkāni": [{ORTH: "rab pilkāni"}],
   "rab pēthalli": [{ORTH: "rab pēthalli"}],
   "rab āpie": [{ORTH: "rab āpie"}],
   "rab ālānāte": [{ORTH: "rab ālānāte"}],
   "rab ālānīšu": [{ORTH: "rab ālānīšu"}],
   "rab nikkassī": [{ORTH: "rab nikkassī"}],
   "rab nikkassi": [{ORTH: "rab nikkassi"}],
   "rab kāru": [{ORTH: "rab kāru"}],
   "rab karāni": [{ORTH: "rab karāni"}],
   "rab kallî":[{ORTH:    "rab kallî"}],
   "rab kallābi":[{ORTH:    "rab kallābi"}],
   "rab kallābāni":[{ORTH:    "rab kallābāni"}],
   "rab mūgiya":[{ORTH:    "rab mūgiya"}],
   "rab mungi":[{ORTH:    "rab mungi"}],
   "rab mūgi":[{ORTH:    "rab mūgi"}],
   "rab mūgīka":[{ORTH:    "rab mūgīka"}],
   "rab kiṣirāni":[{ORTH:    "rab kiṣirāni"}],
   "rab kiṣrāni":[{ORTH:    "rab kiṣrāni"}],
   "rab kiṣrānīya":[{ORTH:    "rab kiṣrānīya"}],
   "rab kiṣrūte":[{ORTH:    "rab kiṣrūte"}],
   "rab kiṣirūtu":[{ORTH:    "rab kiṣirūtu"}],
   "rab kiṣirūte":[{ORTH:    "rab kiṣirūte"}],
   "rab kiṣir":[{ORTH:    "rab kiṣir"}],
   "rab kiṣri":[{ORTH:    "rab kiṣri"}],
   "rab kiṣirūti":[{ORTH:    "rab kiṣirūti"}],
   "rab kaṣir":[{ORTH:    "rab kaṣir"}],
   "rab kāṣir":[{ORTH:    "rab kāṣir"}],
   "rab līm":[{ORTH:    "rab līm"}],
   "rab karkadinni":[{ORTH:    "rab karkadinni"}],
   "rab nuhatimmi":[{ORTH:    "rab nuhatimmi"}],
   "rab etinnāni": [{ORTH: "rab etinnāni"}],
   "rab issāti": [{ORTH: "rab issāti"}],
   "rab bīrti":[{ORTH:    "rab bīrti"}],
   "rab bītīšu":[{ORTH:    "rab bītīšu"}],
   "rab bēti":[{ORTH:    "rab bēti"}],
   "rab bētīya":[{ORTH:    "rab bētīya"}],
   "rab bētīka":[{ORTH:    "rab bētīka"}],
   "rab bīrte":[{ORTH:    "rab bīrte"}],
   "rab birte":[{ORTH:    "rab birte"}],
   "rab līmi":[{ORTH:    "rab līmi"}],
   "rab urāt":[{ORTH:    "rab urāt"}],
   "rab urāte":[{ORTH:    "rab urāte"}],
   "rab urātu":[{ORTH:    "rab urātu"}],
   "rab ālānīma":[{ORTH:    "rab ālānīma"}],
   "rab ālāni":[{ORTH:    "rab ālāni"}],
   "rab ālānišunu":[{ORTH:    "rab ālānišunu"}],
   "rab šāqê":[{ORTH:    "rab šāqê"}],
   "rab kiṣirīya":[{ORTH:    "rab kiṣirīya"}],
   "rab dayālī":[{ORTH:    "rab dayālī"}],
   "rab dayālu": [{ORTH: "rab dayālu"}],
   "rab sakullāte":[{ORTH:    "rab sakullāte"}],
   "rab hanšêkunu":[{ORTH:    "rab hanšêkunu"}],
   "rab danībāte":[{ORTH:    "rab danībāte"}],
   "rab danībāt":[{ORTH:    "rab danībāt"}],
   "rab hanšêya":[{ORTH:    "rab hanšêya"}],
   "rab hanšê": [{ORTH: "rab hanšê"}],
   "rab ešerti": [{ORTH: "rab ešerti"}],
   "rab ešrāte": [{ORTH: "rab ešrāte"}],
   "rab karānī": [{ORTH: "rab karānī"}],
   "rab ṭupšarri": [{ORTH: "rab ṭupšarri"}],
   "rab sinnišāti": [{ORTH: "rab sinnišāti"}],
   "ṭupšar bītūti": [{ORTH: "ṭupšar bītūti"}],
   "ṭupšar bītūtu": [{ORTH: "ṭupšar bītūtu"}],
   "ṭupšar ēkalli": [{ORTH: "ṭupšar ēkalli"}],
   "rādi qāti":[{ORTH:    "rādi qāti"}],
   "rādi imāri":[{ORTH:    "rādi imāri"}],
   "rādi imārī":[{ORTH:    "rādi imārī"}],
   "ṣāb šarrūte":[{ORTH:    "ṣāb šarrūte"}],
   "ṣāb šarri":[{ORTH:    "ṣāb šarri"}],
   "ṣāb šarrīya":[{ORTH:    "ṣāb šarrīya"}],
   "ṣāb šarrēya":[{ORTH:    "ṣāb šarrēya"}],
   "ṣāb šarrišunu":[{ORTH:    "ṣāb šarrišunu"}],
   "ṣāb šarrikunu": [{ORTH: "ṣāb šarrikunu"}],
   "ṣāb šarrišu":[{ORTH:    "ṣāb šarrišu"}],
   "ṣāb šarrišūni":[{ORTH:    "ṣāb šarrišūni"}],
   "ṣābē qalti":[{ORTH:    "ṣābē qalti"}],
   "ṣābē qaltīšu":[{ORTH:    "ṣābē qaltīšu"}],
   "ṣābāni qassi":[{ORTH:    "ṣābāni qassi"}],
   "nīš rēši":[{ORTH:    "nīš rēši"}],
   "ana mēni":[{ORTH:    "ana mēni"}],
   "libīt šarri":[{ORTH:    "libīt šarri"}],
   "lumun libbi":[{ORTH:    "lumun libbi"}],
   "ammat šarri":[{ORTH:    "ammat šarri"}],
   "issi ēkalli":[{ORTH:    "issi ēkalli"}],
   "issu maṣin":[{ORTH:    "issu maṣin"}],
   "amat ēkalli":[{ORTH:    "amat ēkalli"}],
   "marʾat šarri":[{ORTH:    "marʾat šarri"}],
   "mar’ē šīmī":[{ORTH:    "mar’ē šīmī"}],
   "kallāp šibirtu":[{ORTH:    "kallāp šibirtu"}],
   "kallāp šibirti":[{ORTH:    "kallāp šibirti"}],
   "kallāp šibirte":[{ORTH:    "kallāp šibirte"}],
   "kallāp šipirtu":[{ORTH:    "kallāp šipirtu"}],
   "kallāp šipirti":[{ORTH:    "kallāp šipirti"}],
   "nukarib urqi":[{ORTH:    "nukarib urqi"}],
   "dāgil iṣṣūrāti":[{ORTH:    "dāgil iṣṣūrāti"}],
   "dāgil iṣṣūrātišu":[{ORTH:    "dāgil iṣṣūrātišu"}],
   "šākin ṭēmi":[{ORTH:    "šākin ṭēmi"}],
   "šakin māti":[{ORTH:    "šakin māti"}],
   "šakin māt":[{ORTH:    "šakin māt"}],
   "šikin ṭēmi":[{ORTH:    "šikin ṭēmi"}],
   "mašak pīri":[{ORTH:    "mašak pīri"}],
   "ūm eššēši": [{ORTH: "ūm eššēši"}],
   "kaqqad Pazūzāni": [{ORTH: "kaqqad Pazūzāni"}],
   "rab tankārāni": [{ORTH: "rab tankārāni"}],
   "rab karāni": [{ORTH: "rab karāni"}],
   "rab kallābi":[{ORTH:    "rab kallābi"}],
   "rab ša-rēši":[{ORTH:    "rab ša-rēši"}],
   "rab ša-rēšāni":[{ORTH:    "rab ša-rēšāni"}],
   "rab urāsi":[{ORTH:    "rab urāsi"}],
   "rab urāsāni":[{ORTH:    "rab urāsāni"}],
   "rab kāri":[{ORTH:    "rab kāri"}],
   "ab abīni":[{ORTH:    "ab abīni"}],
   "ab abi":[{ORTH:    "ab abi"}],
   "ah abīšu":[{ORTH:    "ah abīšu"}],
   "ab abīya":[{ORTH:    "ab abīya"}],
   "ab abīka":[{ORTH:    "ab abīka"}],
   "ahhē abbēkunu":[{ORTH:    "ahhē abbēkunu"}],
   "ahhē abbēšu":[{ORTH:    "ahhē abbēšu"}],
   "ah abbēšu":[{ORTH:    "ah abbēšu"}],
   "ah abbēka":[{ORTH:    "ah abbēka"}],
   "ālik pāni":[{ORTH:    "ālik pāni"}],
   "ušpār şiprāt": [{ORTH: "ušpār şiprāt"}],
   "ṣalam šarrāni": [{ORTH: "ṣalam šarrāni"}],
   "bēlē piqinnētīšu":[{ORTH:    "bēlē piqinnētīšu"}],
   "bēlē hīṭ":[{ORTH:    "bēlē hīṭ"}],
   "bēlē hiṭṭi":[{ORTH:    "bēlē hiṭṭi"}],
   "bēt erši": [{ORTH: "bēt erši"}],
   "bēt karrāni": [{ORTH: "bēt karrāni"}],
   "bēt šubte":[{ORTH:    "bēt šubte"}],
   "bēti šanie":[{ORTH:    "bēti šanie"}],
   "bīt kunukki":[{ORTH:    "bīt kunukki"}],
   "bēt kunukki":[{ORTH:    "bēt kunukki"}],
   "bīt nakkamdu":[{ORTH:    "bīt nakkamdu"}],
   "bīt ilānīka":[{ORTH:    "bīt ilānīka"}],
   "bēt akīti":[{ORTH:    "bēt akīti"}],
   "bēt dūrāni":[{ORTH:    "bēt dūrāni"}],
   "bēt rēdûte":[{ORTH:    "bēt rēdûte"}],
   "bēt rēdûti":[{ORTH:    "bēt rēdûti"}],
   "bēt šammī": [{ORTH: "bēt šammī"}],
   "bēt šammīya":[{ORTH:    "bēt šammīya"}],
   "bēt rēʾê":[{ORTH:    "bēt rēʾê"}],
   "bēt rēʾî":[{ORTH:    "bēt rēʾî"}],
   "bēt harbi":[{ORTH:    "bēt harbi"}],
   "bīt abīya":[{ORTH:    "bīt abīya"}],
   "bīt abānu":[{ORTH:    "bīt abānu"}],
   "bīt rēdûti":[{ORTH:    "bīt rēdûti"}],
   "bīt ṭabti":[{ORTH:    "bīt ṭabti"}],
   "bīt ṭuppu":[{ORTH:    "bīt ṭuppu"}],
   "bīt killi":[{ORTH:    "bīt killi"}],
   "bīt kīli":[{ORTH:    "bīt kīli"}],
   "bīt kūdanni":[{ORTH:    "bīt kūdanni"}],
   "bēt kutalli": [{ORTH: "bēt kutalli"}],
   "bēt ili":[{ORTH:    "bēt ili"}],
   "bēt isitēya":[{ORTH:    "bēt isitēya"}],
   "bēt abīšu":[{ORTH:    "bēt abīšu"}],
   "bēt mardīti":[{ORTH:    "bēt mardīti"}],
   "bēt mardītīya":[{ORTH:    "bēt mardītīya"}],
   "bēt mardiāti":[{ORTH:    "bēt mardiāti"}],
   "bēt rimki":[{ORTH:    "bēt rimki"}],
   "bēt napṭarte":[{ORTH:    "bēt napṭarte"}],
   "bēt nakkamti":[{ORTH:    "bēt nakkamti"}],
   "bēt qātī":[{ORTH:    "bēt qātī"}],
   "bēt qātīya":[{ORTH:    "bēt qātīya"}],
   "bēt mayālīya":[{ORTH:    "bēt mayālīya"}],
   "bēt bēlīšu":[{ORTH:    "bēt bēlīšu"}],
   "bēt bēlī":[{ORTH:    "bēt bēlī"}],
   "bēt bēlēka":[{ORTH:    "bēt bēlēka"}],
   "bēt bēlēya":[{ORTH:    "bēt bēlēya"}],
   "bēt bēlīkunu":[{ORTH:    "bēt bēlīkunu"}],
   "bēt ilānišu":[{ORTH:    "bēt ilānišu"}],
   "bēt ilāni":[{ORTH:    "bēt ilāni"}],
   "bīt ili":[{ORTH:    "bīt ili"}],
   "bīt ilāni":[{ORTH:    "bīt ilāni"}],
   "bīt nakkamti":[{ORTH:    "bīt nakkamti"}],
   "ērib ēkalli":[{ORTH:    "ērib ēkalli"}],
   "ēribūti bīti": [{ORTH: "ēribūti bīti"}],
   "ērib bēti": [{ORTH: "ērib bēti"}],
   "ērib bīti": [{ORTH: "ērib bīti"}],
   "ērib bītāti": [{ORTH: "ērib bītāti"}],
   "zēr šarri":[{ORTH:    "zēr šarri"}],
   "kî mādê":[{ORTH:    "kî mādê"}],
   "manzāza pāni":[{ORTH:    "manzāza pāni"}],
   "mār muškēnūti":[{ORTH:    "mār muškēnūti"}],
   "mār nagie":[{ORTH:    "mār nagie"}],
   "mār banî":[{ORTH:    "mār banî"}],
   "mār mārīka":[{ORTH:    "mār mārīka"}],
   "mārē banê":[{ORTH:    "mārē banê"}],
   "mārē banê":[{ORTH:    "mārē banê"}],
   "mārē banî":[{ORTH:    "mārē banî"}],
   "mārē babili":[{ORTH:    "mārē babili"}],
   "mār banê":[{ORTH:    "mār banê"}],
   "mār Babila":[{ORTH:    "mār Babila"}],
   "mār Barsip": [{ORTH: "mār Barsip"}],
   "mār ahhē abbēšu":[{ORTH:    "mār ahhē abbēšu"}],
   "mār šarrūti": [{ORTH: "mār šarrūti"}],
   "mār šarrūte": [{ORTH: "mār šarrūte"}],
   "mār šarri":[{ORTH:    "mār šarri"}],
   "mārat šarri":[{ORTH:    "mārat šarri"}],
   "marʾē šarri":[{ORTH:    "marʾē šarri"}],
   "mār kitkittê":[{ORTH:    "mār kitkittê"}],
   "mār ahātīya":[{ORTH:    "mār ahātīya"}],
   "mār ahīšu":[{ORTH:    "mār ahīšu"}],
   "mār šiprešunu":[{ORTH:    "mār šiprešunu"}],
   "mār šiprātēya":[{ORTH:    "mār šiprātēya"}],
   "mār šipru":[{ORTH:    "mār šipru"}],
   "mār šipri":[{ORTH:    "mār šipri"}],
   "mār šiprāta":[{ORTH:    "mār šiprāta"}],
   "mār šiprānūwa":[{ORTH:    "mār šiprānūwa"}],
   "mār šiprīya":[{ORTH:    "mār šiprīya"}],
   "mār šiprēya": [{ORTH: "mār šiprēya"}],
   "mār šiprāni":[{ORTH:    "mār šiprāni"}],
   "mār šiprīni": [{ORTH: "mār šiprīni"}],
   "mār šiprānīni":[{ORTH:    "mār šiprānīni"}],
   "mār šiprānīšu":[{ORTH:    "mār šiprānīšu"}],
   "mār šiprānīka":[{ORTH:    "mār šiprānīka"}],
   "mār šiprānīya":[{ORTH:    "mār šiprānīya"}],
   "mār šiprīka":[{ORTH:    "mār šiprīka"}],
   "mār šiprīšu":[{ORTH:    "mār šiprīšu"}],
   "mār šiprēšu":[{ORTH:    "mār šiprēšu"}],
   "mār šiprišunu":[{ORTH:    "mār šiprišunu"}],
   "mār šiprānišunu":[{ORTH:    "mār šiprānišunu"}],
   "mār šiprātišunu":[{ORTH:    "mār šiprātišunu"}],
   "mār šiprikunu":[{ORTH:    "mār šiprikunu"}],
   "mār šīmi":[{ORTH:    "mār šīmi"}],
   "mār damqi":[{ORTH:    "mār damqi"}],
   "mār damqūti":[{ORTH:    "mār damqūti"}],
   "mār damqūte": [{ORTH: "mār damqūte"}],
   "mār damqīya":[{ORTH:    "mār damqīya"}],
   "mār Babili":[{ORTH:    "mār Babili"}],
   "mutīr ṭēme":[{ORTH:    "mutīr ṭēme"}],
   "mutīr ṭēmu":[{ORTH:    "mutīr ṭēmu"}],
   "mutīr ṭēmi":[{ORTH:    "mutīr ṭēmi"}],
   "mukīl rēš": [{ORTH: "mukīl rēš"}],
   "mukīl pāni": [{ORTH: "mukīl pāni"}],
   "mukīl appāni":[{ORTH:    "mukīl appāni"}],
   "mukīl appāti":[{ORTH:    "mukīl appāti"}],
   "mukīl appātīya":[{ORTH:    "mukīl appātīya"}],
   "mukīl appātūtu":[{ORTH:    "mukīl appātūtu"}],
   "Māt-Aššur":[{ORTH:    "Māt-Aššur"}],
   "Māt Aššur":[{ORTH:    "Māt Aššur"}],
   "šikin ṭēmūti":[{ORTH:    "šikin ṭēmūti"}],
   "šikin ṭēmišunu":[{ORTH:    "šikin ṭēmišunu"}],
   "šikin ṭēmīni":[{ORTH:    "šikin ṭēmīni"}],
   "qabsi āli":[{ORTH:    "qabsi āli"}],
   "nāgir ēkalli":[{ORTH:    "nāgir ēkalli"}],
   "hūl šarri":[{ORTH:    "hūl šarri"}],
   "hūl šarrāni":[{ORTH:    "hūl šarrāni"}],
   "hūlāni šarrāni":[{ORTH:    "hūlāni šarrāni"}],
   "urdu ēkalli":[{ORTH:    "urdu ēkalli"}],
   "{1}x+x":[{ORTH:    "{1}x+x"}],
   "{1}x":[{ORTH:    "{1}x"}],
   "{d}x":[{ORTH:    "{d}x"}],
   "{d}x+x":[{ORTH:    "{d}x+x"}],
   "{KUR}x":[{ORTH:    "{KUR}x"}],
   "{KUR}x+x":[{ORTH:    "{KUR}x+x"}],
   "{URU}x":[{ORTH:    "{URU}x"}],
   "{URU}x+x":[{ORTH:    "{URU}x+x"}],
   "{1}{d}x":[{ORTH:    "{1}{d}x"}],
   "{1}{d}x+x":[{ORTH:    "{1}{d}x+x"}],
   "{LU₂}x":[{ORTH:    "{LU₂}x"}],
   "{LU₂}x+x":[{ORTH:    "{LU₂}x+x"}],
   "x-KAM":[{ORTH:    "x-KAM"}],
   "x-KAM₂":[{ORTH:    "x-KAM₂"}],
   "UD-x-KAM":[{ORTH:    "UD-x-KAM"}],
   "issu mar":[{ORTH:    "issu mar"}],



}


]

TOKENIZER_EXCEPTIONS = update_exc(BASE_EXCEPTIONS, *exclusions)
