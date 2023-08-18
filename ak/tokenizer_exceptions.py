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
   "bēl šemērē":[{ORTH:    "bēl šemērē"}],
   "bēl adê":[{ORTH:    "bēl adê"}],
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
   "bēl salāmīšu":[{ORTH:    "bēl salāmīšu"}],
   "bēl salāmīni":[{ORTH:    "bēl salāmīni"}],
   "bēl ṣāssi":[{ORTH:    "bēl ṣāssi"}],
   "bēl habulli":[{ORTH:    "bēl habulli"}],
   "bēl ṣāssīšunu":[{ORTH:    "bēl ṣāssīšunu"}],
   "bēl habullīšunu":[{ORTH:    "bēl habullīšunu"}],
   "bēl pīhāti":[{ORTH:    "bēl pīhāti"}],
   "bēl piqitti":[{ORTH:    "bēl piqitti"}],
   "bēl piqittāti":[{ORTH:    "bēl piqittāti"}],
   "bēl piqittīya":[{ORTH:    "bēl piqittīya"}],
   "bēl piqittēya":[{ORTH:    "bēl piqittēya"}],
   "bēl piqittāte":[{ORTH:    "bēl piqittāte"}],
   "bēl ālāni":[{ORTH:    "bēl ālāni"}],
   "bēl ālūtê":[{ORTH:    "bēl ālūtê"}],
   "bēl āli":[{ORTH:    "bēl āli"}],
   "bēl dēnīšu":[{ORTH:    "bēl dēnīšu"}],
   "bēl dīnīya":[{ORTH:    "bēl dīnīya"}],
   "bēl ṭābātekunu":[{ORTH:    "bēl ṭābātekunu"}],
   "bēl ṣāltīya": [{ORTH: "bēl ṣāltīya"}],
   "bēl ṣēlti": [{ORTH: "bēl ṣēlti"}],
   "bēl ṭābti":[{ORTH:    "bēl ṭābti"}],
   "bēl ṭābtīya":[{ORTH:    "bēl ṭābtīya"}],
   "bēl tahūmešunu":[{ORTH:    "bēl tahūmešunu"}],
   "bēlē ṭābtēya":[{ORTH:    "bēlē ṭābtēya"}],
   "bēlē ṭābti":[{ORTH:    "bēlē ṭābti"}],
   "arû šūluk":[{ORTH:    "arû šūluk"}],
   "ummi šarri":[{ORTH:    "ummi šarri"}],
   "ummi abīšu":[{ORTH:    "ummi abīšu"}],
   "šamnu ṭābu":[{ORTH:    "šamnu ṭābu"}],
   "ṣīt libbīya":[{ORTH:    "ṣīt libbīya"}],
   "ṣīt Šamaš":[{ORTH:    "ṣīt Šamaš"}],
   "mazzāz pāni":[{ORTH:    "mazzāz pāni"}],
   "ēkal māšarti":[{ORTH:    "ēkal māšarti"}],
   "manzāz ēkalli": [{ORTH: "manzāz ēkalli"}],
   "kal ūme": [{ORTH: "kal ūme"}],
   "rab qalti": [{ORTH: "rab qalti"}],
   "rab qašti": [{ORTH: "rab qašti"}],
   "rab bīti": [{ORTH: "rab bīti"}],
   "rab ēkalli": [{ORTH: "rab ēkalli"}],
   "rab pēthalli": [{ORTH: "rab pēthalli"}],
   "rab ālānāte": [{ORTH: "rab ālānāte"}],
   "rab nikkassī": [{ORTH: "rab nikkassī"}],
   "rab nikkassi": [{ORTH: "rab nikkassi"}],
   "rab kāru": [{ORTH: "rab kāru"}],
   "rab karāni": [{ORTH: "rab karāni"}],
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
   "rab kiṣirūte":[{ORTH:    "rab kiṣirūte"}],
   "rab kiṣir":[{ORTH:    "rab kiṣir"}],
   "rab kiṣri":[{ORTH:    "rab kiṣri"}],
   "rab kiṣirūti":[{ORTH:    "rab kiṣirūti"}],
   "rab kaṣir":[{ORTH:    "rab kaṣir"}],
   "rab kāṣir":[{ORTH:    "rab kāṣir"}],
   "rab līm":[{ORTH:    "rab līm"}],
   "rab karkadinni":[{ORTH:    "rab karkadinni"}],
   "rab nuhatimmi":[{ORTH:    "rab nuhatimmi"}],
   "rab issāti": [{ORTH: "rab issāti"}],
   "rab bīrti":[{ORTH:    "rab bīrti"}],
   "rab bītīšu":[{ORTH:    "rab bītīšu"}],
   "rab bēti":[{ORTH:    "rab bēti"}],
   "rab bētīya":[{ORTH:    "rab bētīya"}],
   "rab bētīka":[{ORTH:    "rab bētīka"}],
   "rab birte":[{ORTH:    "rab birte"}],
   "rab urāte":[{ORTH:    "rab urāte"}],
   "rab urātu":[{ORTH:    "rab urātu"}],
   "rab ālānīma":[{ORTH:    "rab ālānīma"}],
   "rab ālāni":[{ORTH:    "rab ālāni"}],
   "rab ālānišunu":[{ORTH:    "rab ālānišunu"}],
   "rab šāqê":[{ORTH:    "rab šāqê"}],
   "rab kiṣirīya":[{ORTH:    "rab kiṣirīya"}],
   "rab dayālī":[{ORTH:    "rab dayālī"}],
   "rab sakullāte":[{ORTH:    "rab sakullāte"}],
   "rab hanšêkunu":[{ORTH:    "rab hanšêkunu"}],
   "rab danībāt":[{ORTH:    "rab danībāt"}],
   "rab hanšêya":[{ORTH:    "rab hanšêya"}],
   "rab hanšê": [{ORTH: "rab hanšê"}],
   "rab ešerti": [{ORTH: "rab ešerti"}],
   "rab ešrāte": [{ORTH: "rab ešrāte"}],
   "rab karānī": [{ORTH: "rab karānī"}],
   "rab ṭupšarri": [{ORTH: "rab ṭupšarri"}],
   "ṭupšar bītūti": [{ORTH: "ṭupšar bītūti"}],
   "ṭupšar bītūtu": [{ORTH: "ṭupšar bītūtu"}],
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
   "nīš rēši":[{ORTH:    "nīš rēši"}],
   "ana mēni":[{ORTH:    "ana mēni"}],
   "libīt šarri":[{ORTH:    "libīt šarri"}],
   "lumun libbi":[{ORTH:    "lumun libbi"}],
   "ammat šarri":[{ORTH:    "ammat šarri"}],
   "issi ēkalli":[{ORTH:    "issi ēkalli"}],
   "issu maṣin":[{ORTH:    "issu maṣin"}],
   "amat ēkalli":[{ORTH:    "amat ēkalli"}],
   "mar’ē šīmī":[{ORTH:    "mar’ē šīmī"}],
   "kallāp šibirtu":[{ORTH:    "kallāp šibirtu"}],
   "kallāp šibirti":[{ORTH:    "kallāp šibirti"}],
   "kallāp šibirte":[{ORTH:    "kallāp šibirte"}],
   "kallāp šipirtu":[{ORTH:    "kallāp šipirtu"}],
   "kallāp šipirti":[{ORTH:    "kallāp šipirti"}],
   "nukarib urqi":[{ORTH:    "nukarib urqi"}],
   "dāgil iṣṣūrāti":[{ORTH:    "dāgil iṣṣūrāti"}],
   "šākin ṭēmi":[{ORTH:    "šākin ṭēmi"}],
   "šakin māti":[{ORTH:    "šakin māti"}],
   "šakin māt":[{ORTH:    "šakin māt"}],
   "šikin ṭēmi":[{ORTH:    "šikin ṭēmi"}],
   "mašak pīri":[{ORTH:    "mašak pīri"}],
   "ūm eššēši": [{ORTH: "ūm eššēši"}],
   "rab tankārāni": [{ORTH: "rab tankārāni"}],
   "rab karāni": [{ORTH: "rab karāni"}],
   "rab kallābi":[{ORTH:    "rab kallābi"}],
   "rab ša-rēši":[{ORTH:    "rab ša-rēši"}],
   "rab ša-rēšāni":[{ORTH:    "rab ša-rēšāni"}],
   "rab urāsi":[{ORTH:    "rab urāsi"}],
   "rab urāsāni":[{ORTH:    "rab urāsāni"}],
   "rab kāri":[{ORTH:    "rab kāri"}],
   "ab abi":[{ORTH:    "ab abi"}],
   "ah abīšu":[{ORTH:    "ah abīšu"}],
   "ab abīya":[{ORTH:    "ab abīya"}],
   "ab abīka":[{ORTH:    "ab abīka"}],
   "ahhē abbēkunu":[{ORTH:    "ahhē abbēkunu"}],
   "ahhē abbēšu":[{ORTH:    "ahhē abbēšu"}],
   "ah abbēšu":[{ORTH:    "ah abbēšu"}],
   "ah abbēka":[{ORTH:    "ah abbēka"}],
   "ušpār şiprāt": [{ORTH: "ušpār şiprāt"}],
   "ṣalam šarrāni": [{ORTH: "ṣalam šarrāni"}],
   "bēlē piqinnētīšu":[{ORTH:    "bēlē piqinnētīšu"}],
   "bēlē hīṭ":[{ORTH:    "bēlē hīṭ"}],
   "bēt šubte":[{ORTH:    "bēt šubte"}],
   "bēti šanie":[{ORTH:    "bēti šanie"}],
   "bīt nakkamdu":[{ORTH:    "bīt nakkamdu"}],
   "bīt ilānīka":[{ORTH:    "bīt ilānīka"}],
   "bēt akīti":[{ORTH:    "bēt akīti"}],
   "bēt dūrāni":[{ORTH:    "bēt dūrāni"}],
   "bēt rēdûte":[{ORTH:    "bēt rēdûte"}],
   "bēt rēdûti":[{ORTH:    "bēt rēdûti"}],
   "bīt abānu":[{ORTH:    "bīt abānu"}],
   "bīt rēdûti":[{ORTH:    "bīt rēdûti"}],
   "bīt ṭabti":[{ORTH:    "bīt ṭabti"}],
   "bīt killi":[{ORTH:    "bīt killi"}],
   "bīt kīli":[{ORTH:    "bīt kīli"}],
   "bēt kutalli": [{ORTH: "bēt kutalli"}],
   "bēt ili":[{ORTH:    "bēt ili"}],
   "bēt isitēya":[{ORTH:    "bēt isitēya"}],
   "bēt abīšu":[{ORTH:    "bēt abīšu"}],
   "bēt mardīti":[{ORTH:    "bēt mardīti"}],
   "bēt mardītīya":[{ORTH:    "bēt mardītīya"}],
   "bēt rimki":[{ORTH:    "bēt rimki"}],
   "bēt nakkamti":[{ORTH:    "bēt nakkamti"}],
   "bēt qātī":[{ORTH:    "bēt qātī"}],
   "bēt qātīya":[{ORTH:    "bēt qātīya"}],
   "bēt mayālīya":[{ORTH:    "bēt mayālīya"}],
   "bēt bēlī":[{ORTH:    "bēt bēlī"}],
   "bēt bēlēka":[{ORTH:    "bēt bēlēka"}],
   "bēt bēlīkunu":[{ORTH:    "bēt bēlīkunu"}],
   "bēt ilāni":[{ORTH:    "bēt ilāni"}],
   "bīt ili":[{ORTH:    "bīt ili"}],
   "bīt ilāni":[{ORTH:    "bīt ilāni"}],
   "bīt nakkamti":[{ORTH:    "bīt nakkamti"}],
   "ērib ēkalli":[{ORTH:    "ērib ēkalli"}],
   "ēribūti bīti": [{ORTH: "ēribūti bīti"}],
   "ērib bīti": [{ORTH: "ērib bīti"}],
   "ērib bītāti": [{ORTH: "ērib bītāti"}],
   "zēr šarri":[{ORTH:    "zēr šarri"}],
   "kî mādê":[{ORTH:    "kî mādê"}],
   "manzāza pāni":[{ORTH:    "manzāza pāni"}],
   "mār muškēnūti":[{ORTH:    "mār muškēnūti"}],
   "mār banî":[{ORTH:    "mār banî"}],
   "mār mārīka":[{ORTH:    "mār mārīka"}],
   "mārē banî":[{ORTH:    "mārē banî"}],
   "mār banê":[{ORTH:    "mār banê"}],
   "mār Babila":[{ORTH:    "mār Babila"}],
   "mār ahhē abbēšu":[{ORTH:    "mār ahhē abbēšu"}],
   "mār šarrūti": [{ORTH: "mār šarrūti"}],
   "mār šarrūte": [{ORTH: "mār šarrūte"}],
   "mār šarri":[{ORTH:    "mār šarri"}],
   "marʾē šarri":[{ORTH:    "marʾē šarri"}],
   "mār kitkittê":[{ORTH:    "mār kitkittê"}],
   "mār ahīšu":[{ORTH:    "mār ahīšu"}],
   "mār šipri":[{ORTH:    "mār šipri"}],
   "mār šiprāta":[{ORTH:    "mār šiprāta"}],
   "mār šiprīya":[{ORTH:    "mār šiprīya"}],
   "mār šiprēya": [{ORTH: "mār šiprēya"}],
   "mār šiprāni":[{ORTH:    "mār šiprāni"}],
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
   "mār šīmi":[{ORTH:    "mār šīmi"}],
   "mār damqi":[{ORTH:    "mār damqi"}],
   "mār damqūti":[{ORTH:    "mār damqūti"}],
   "mār damqūte": [{ORTH: "mār damqūte"}],
   "mār damqīya":[{ORTH:    "mār damqīya"}],
   "mār Babili":[{ORTH:    "mār Babili"}],
   "mutīr ṭēme":[{ORTH:    "mutīr ṭēme"}],
   "mukīl appāni":[{ORTH:    "mukīl appāni"}],
   "mukīl appāti":[{ORTH:    "mukīl appāti"}],
   "mukīl appātīya":[{ORTH:    "mukīl appātīya"}],
   "mukīl appātūtu":[{ORTH:    "mukīl appātūtu"}],
   "Māt-Aššur":[{ORTH:    "Māt-Aššur"}],
   "Māt Aššur":[{ORTH:    "Māt Aššur"}],
   "šikin ṭēmūti":[{ORTH:    "šikin ṭēmūti"}],
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
   "Aššur-dur-paniya":[{ORTH:"Aššur-dur-paniya"}],
   "Nabu-hammatua":[{ORTH:"Nabu-hammatua"}],
   "Hu-Teššub":[{ORTH:"Hu-Teššub"}],
   "Ammi-raʾi":[{ORTH:"Ammi-raʾi"}],
   "Nabu-hamatua":[{ORTH:"Nabu-hamatua"}],
   "Kar-Nergal":[{ORTH:"Kar-Nergal"}],
   "Aššur-remanni":[{ORTH:"Aššur-remanni"}],
   "Nabu-remanni":[{ORTH:"Nabu-remanni"}],
   "Abat-šarri-uṣur":[{ORTH:"Abat-šarri-uṣur"}],
   "Hu-Teššubu":[{ORTH:"Hu-Teššubu"}],
   "Šamaš-išmanni":[{ORTH:"Šamaš-išmanni"}],
   "Bel-qatua":[{ORTH:"Bel-qatua"}],
   "Gabbu-amur":[{ORTH:"Gabbu-amur"}],
   "Adad-aplu-iddina":[{ORTH:"Adad-aplu-iddina"}],
   "Iqiša-Marduk":[{ORTH:"Iqiša-Marduk"}],
   "Nabu-ahu-uṣur":[{ORTH:"Nabu-ahu-uṣur"}],
   "Attar-ham":[{ORTH:"Attar-ham"}],
   "Ilu-illika":[{ORTH:"Ilu-illika"}],
   "Kar-Šamaš":[{ORTH:"Kar-Šamaš"}],
   "Šulmu-beli-lašme":[{ORTH:"Šulmu-beli-lašme"}],
   "Aššur-alik-pani":[{ORTH:"Aššur-alik-pani"}],
   "Abu-ul-idi":[{ORTH:"Abu-ul-idi"}],
   "Aššur-balti-niše":[{ORTH:"Aššur-balti-niše"}],
   "Aššur-bessunu":[{ORTH:"Aššur-bessunu"}],
   "Gabbu-ana-Aššur":[{ORTH:"Gabbu-ana-Aššur"}],
   "Ša-ili-dubbu":[{ORTH:"Ša-ili-dubbu"}],
   "Nergal-šarrani":[{ORTH:"Nergal-šarrani"}],
   "Aššur-leʾi":[{ORTH:"Aššur-leʾi"}],
   "Zaba-iqiša":[{ORTH:"Zaba-iqiša"}],
   "Issar-duri":[{ORTH:"Issar-duri"}],
   "Urdu-Sin":[{ORTH:"Urdu-Sin"}],
   "Mannu-ki-Adad":[{ORTH:"Mannu-ki-Adad"}],
   "Bel-ahhe":[{ORTH:"Bel-ahhe"}],
   "Nergal-eṭir":[{ORTH:"Nergal-eṭir"}],
   "Dur-Yakinaya":[{ORTH:"Dur-Yakinaya"}],
   "Bit-Abdadani":[{ORTH:"Bit-Abdadani"}],
   "Nergal-belu-uṣur":[{ORTH:"Nergal-belu-uṣur"}],
   "Nabu-zeru-iddina":[{ORTH:"Nabu-zeru-iddina"}],
   "Mannu-ki-ahhe":[{ORTH:"Mannu-ki-ahhe"}],
   "Šarru-emuranni":[{ORTH:"Šarru-emuranni"}],
   "Atta-idri":[{ORTH:"Atta-idri"}],
   "mar-Babili":[{ORTH:"mar-Babili"}],
   "Bel-iddina":[{ORTH:"Bel-iddina"}],
   "Aššur-šarru-uṣur":[{ORTH:"Aššur-šarru-uṣur"}],
   "Mat-Aššur":[{ORTH:"Mat-Aššur"}],
   "Il-dala":[{ORTH:"Il-dala"}],
   "Nabu-uṣalla":[{ORTH:"Nabu-uṣalla"}],
   "Dur-Šamaš":[{ORTH:"Dur-Šamaš"}],
   "Nabu-ereš":[{ORTH:"Nabu-ereš"}],
   "Aššur-reṣuwa":[{ORTH:"Aššur-reṣuwa"}],
   "Mušallim-Adad":[{ORTH:"Mušallim-Adad"}],
   "Kar-siparri":[{ORTH:"Kar-siparri"}],
   "Silim-Aššur":[{ORTH:"Silim-Aššur"}],
   "Šamaš-ukin":[{ORTH:"Šamaš-ukin"}],
   "Adad-isseʾa":[{ORTH:"Adad-isseʾa"}],
   "Kubaba-ilaʾi":[{ORTH:"Kubaba-ilaʾi"}],
   "Halzi-atbar":[{ORTH:"Halzi-atbar"}],
   "Bit-Hamban":[{ORTH:"Bit-Hamban"}],
   "Aššur-zeru-ibni":[{ORTH:"Aššur-zeru-ibni"}],
   "Haldi-abu-uṣur":[{ORTH:"Haldi-abu-uṣur"}],
   "Aššur-šarrani":[{ORTH:"Aššur-šarrani"}],
   "Duri-Adad":[{ORTH:"Duri-Adad"}],
   "Kubaba-satar":[{ORTH:"Kubaba-satar"}],
   "Išmanni-Aššur":[{ORTH:"Išmanni-Aššur"}],
   "mare-Babili":[{ORTH:"mare-Babili"}],
   "Bit-Zamana":[{ORTH:"Bit-Zamana"}],
   "Kiṣir-Aššur":[{ORTH:"Kiṣir-Aššur"}],
   "Upaq-Šamaš":[{ORTH:"Upaq-Šamaš"}],
   "Ubru-Harran":[{ORTH:"Ubru-Harran"}],
   "Naṣib-il":[{ORTH:"Naṣib-il"}],
   "Bit-Ukannaya":[{ORTH:"Bit-Ukannaya"}],
   "Meṣate-ibni":[{ORTH:"Meṣate-ibni"}],
   "Naʾdi-ilu":[{ORTH:"Naʾdi-ilu"}],
   "Nabu-ušabši":[{ORTH:"Nabu-ušabši"}],
   "Atanha-Šamaš":[{ORTH:"Atanha-Šamaš"}],
   "Dur-Atanate":[{ORTH:"Dur-Atanate"}],
   "Šarru-iqbi":[{ORTH:"Šarru-iqbi"}],
   "Bit-Zamani":[{ORTH:"Bit-Zamani"}],
   "Ša-Aššur-dubbu":[{ORTH:"Ša-Aššur-dubbu"}],
   "Dur-Yakini":[{ORTH:"Dur-Yakini"}],
   "Tarditu-Aššur":[{ORTH:"Tarditu-Aššur"}],
   "Marduk-remanni":[{ORTH:"Marduk-remanni"}],
   "Seʾ-gabbar":[{ORTH:"Seʾ-gabbar"}],
   "Issar-šumu-iqiša":[{ORTH:"Issar-šumu-iqiša"}],
   "Šulmu-beli":[{ORTH:"Šulmu-beli"}],
   "Taklak-ana-Bel":[{ORTH:"Taklak-ana-Bel"}],
   "Ṭab-šar-Aššur":[{ORTH:"Ṭab-šar-Aššur"}],
   "Nabu-eriba":[{ORTH:"Nabu-eriba"}],
   "Aššur-belu-daʾʾin":[{ORTH:"Aššur-belu-daʾʾin"}],
   "Nabu-leʾi":[{ORTH:"Nabu-leʾi"}],
   "Mar-Issar":[{ORTH:"Mar-Issar"}],
   "Išme-ilu":[{ORTH:"Išme-ilu"}],
   "Nabu-šarru-uṣur":[{ORTH:"Nabu-šarru-uṣur"}],
   "Sin-ahhe-eriba":[{ORTH:"Sin-ahhe-eriba"}],
   "Adad-remanni":[{ORTH:"Adad-remanni"}],
   "Aššur-patinu":[{ORTH:"Aššur-patinu"}],
   "Bel-emuranni":[{ORTH:"Bel-emuranni"}],
   "Dala-il":[{ORTH:"Dala-il"}],
   "Adad-ibni":[{ORTH:"Adad-ibni"}],
   "Abi-rame":[{ORTH:"Abi-rame"}],
   "Dur-Taliti":[{ORTH:"Dur-Taliti"}],
   "Mannu-ki-Arbail":[{ORTH:"Mannu-ki-Arbail"}],
   "Dur-Šarruken":[{ORTH:"Dur-Šarruken"}],
   "Nashir-Bel":[{ORTH:"Nashir-Bel"}],
   "Aššur-belu-udaʾʾan":[{ORTH:"Aššur-belu-udaʾʾan"}],
   "Abi-yaqa":[{ORTH:"Abi-yaqa"}],
   "Šamaš-belu-uṣur":[{ORTH:"Šamaš-belu-uṣur"}],
   "Halzi-atbaraya":[{ORTH:"Halzi-atbaraya"}],
   "Ea-šarru-ibni":[{ORTH:"Ea-šarru-ibni"}],
   "Qurdi-Issar":[{ORTH:"Qurdi-Issar"}],
   "Ubru-Palil":[{ORTH:"Ubru-Palil"}],
   "Šamaš-ilaʾi":[{ORTH:"Šamaš-ilaʾi"}],
   "Kar-Aššur":[{ORTH:"Kar-Aššur"}],


}


]

TOKENIZER_EXCEPTIONS = update_exc(BASE_EXCEPTIONS, *exclusions)
