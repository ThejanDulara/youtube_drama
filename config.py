import os

DRAMAS = [
    # ================= HIRU TV =================
    {
        "drama_key": "paata_kurullo",
        "drama_name": "Paata Kurullo (පාට කුරුල්ලෝ)",
        "channel_key": "hiru",
        "channel_name": "HIRU TV",
        "channel_id": "UCOtYyt7W5PmPnwQjWWF_Z-Q",
        "title_keywords": ["Paata Kurullo", "පාට කුරුල්ලෝ"],
    },
    {
        "drama_key": "akurata_yana_welawe",
        "drama_name": "Akurata Yana Welawe (අකුරට යන වෙලාවේ)",
        "channel_key": "hiru",
        "channel_name": "HIRU TV",
        "channel_id": "UCOtYyt7W5PmPnwQjWWF_Z-Q",
        "title_keywords": ["Akurata Yana Welawe", "අකුරට යන වෙලාවේ"],
    },
    {
        "drama_key": "ron_soyaa",
        "drama_name": "Ron Soyaa (රොන් සොයා)",
        "channel_key": "hiru",
        "channel_name": "HIRU TV",
        "channel_id": "UCOtYyt7W5PmPnwQjWWF_Z-Q",
        "title_keywords": ["Ron Soyaa", "රොන් සොයා"],
    },
    {
        "drama_key": "tharu_adare",
        "drama_name": "Tharu Adare (තරු ආදරේ)",
        "channel_key": "hiru",
        "channel_name": "HIRU TV",
        "channel_id": "UCOtYyt7W5PmPnwQjWWF_Z-Q",
        "title_keywords": ["Tharu Adare", "තරු ආදරේ"],
    },
    {
        "drama_key": "chanchala_rekha",
        "drama_name": "Chanchala Rekha (චංචල රේඛා)",
        "channel_key": "hiru",
        "channel_name": "HIRU TV",
        "channel_id": "UCOtYyt7W5PmPnwQjWWF_Z-Q",
        "title_keywords": ["Chanchala Rekha", "චංචල රේඛා"],
    },
    {
        "drama_key": "oba_enna_awith_yanna",
        "drama_name": "Oba Enna Awith Yanna (ඔබ එන්න ඇවිත් යන්න)",
        "channel_key": "hiru",
        "channel_name": "HIRU TV",
        "channel_id": "UCOtYyt7W5PmPnwQjWWF_Z-Q",
        "title_keywords": ["Oba Enna Awith Yanna", "ඔබ එන්න ඇවිත් යන්න"],
    },

    # ================= DERANA =================
    {
        "drama_key": "iskole",
        "drama_name": "Iskole (ඉස්කෝලේ)",
        "channel_key": "derana",
        "channel_name": "DERANA",
        "channel_id": "UCRDDfbYPHX_GUJ4lcQYTc8A",
        "title_keywords": ["Iskole", "ඉස්කෝලේ"],
    },
    {
        "drama_key": "sangeethe",
        "drama_name": "Sangeethe (සංගීතේ)",
        "channel_key": "derana",
        "channel_name": "DERANA",
        "channel_id": "UC0f3jD9QZsKxQ0T5QZxXzRw",
        "title_keywords": ["Sangeethe", "සංගීතේ"],
    },
    {
        "drama_key": "deweni_inima",
        "drama_name": "Deweni Inima (දෙවෙනි ඉනිම)",
        "channel_key": "derana",
        "channel_name": "DERANA",
        "channel_id": "UC0f3jD9QZsKxQ0T5QZxXzRw",
        "title_keywords": ["Deweni Inima", "දෙවෙනි ඉනිම"],
    },
    {
        "drama_key": "hithagannama_bari_kathawak",
        "drama_name": "Hithagannama Bari Kathawak (හිතාගන්නම බැරි කතාවක්)",
        "channel_key": "derana",
        "channel_name": "DERANA",
        "channel_id": "UC0f3jD9QZsKxQ0T5QZxXzRw",
        "title_keywords": ["Hithagannama Bari Kathawak", "හිතාගන්නම බැරි කතාවක්"],
    },
    {
        "drama_key": "man_adarei",
        "drama_name": "Man Adarei (මං ආදරෙයි)",
        "channel_key": "derana",
        "channel_name": "DERANA",
        "channel_id": "UC0f3jD9QZsKxQ0T5QZxXzRw",
        "title_keywords": ["Man Adarei", "මං ආදරෙයි"],
    },
    {
        "drama_key": "thappara_katta",
        "drama_name": "Thappara Katta (තප්පර කට්ටා)",
        "channel_key": "derana",
        "channel_name": "DERANA",
        "channel_id": "UC0f3jD9QZsKxQ0T5QZxXzRw",
        "title_keywords": ["Thappara Katta", "තප්පර කට්ටා"],
    },

    # ================= SIRASA TV =================
    {
        "drama_key": "kalu_ahasa",
        "drama_name": "Kalu Ahasa (කළු අහස)",
        "channel_key": "sirasa",
        "channel_name": "SIRASA TV",
        "channel_id": "UC4HxYf6GZ0sZ5m2b0k8z5xA",
        "title_keywords": ["Kalu Ahasa", "කළු අහස"],
    },
    {
        "drama_key": "aaley",
        "drama_name": "Aaley (ආලේ)",
        "channel_key": "sirasa",
        "channel_name": "SIRASA TV",
        "channel_id": "UC4HxYf6GZ0sZ5m2b0k8z5xA",
        "title_keywords": ["Aaley", "ආලේ"],
    },
    {
        "drama_key": "maayavi",
        "drama_name": "Maayavi (මායාවී)",
        "channel_key": "sirasa",
        "channel_name": "SIRASA TV",
        "channel_id": "UC4HxYf6GZ0sZ5m2b0k8z5xA",
        "title_keywords": ["Maayavi", "මායාවී"],
    },
    {
        "drama_key": "aalawanthi",
        "drama_name": "Aalawanthi (ආලවන්තී)",
        "channel_key": "sirasa",
        "channel_name": "SIRASA TV",
        "channel_id": "UC4HxYf6GZ0sZ5m2b0k8z5xA",
        "title_keywords": ["Aalawanthi", "ආලවන්තී"],
    },
    {
        "drama_key": "kotu",
        "drama_name": "Kotu (කොටු)",
        "channel_key": "sirasa",
        "channel_name": "SIRASA TV",
        "channel_id": "UC4HxYf6GZ0sZ5m2b0k8z5xA",
        "title_keywords": ["Kotu", "කොටු"],
    },

    # ================= SWARNAVAHINI =================
    {
        "drama_key": "sinto",
        "drama_name": "Sinto (සින්ටෝ)",
        "channel_key": "swarnavahini",
        "channel_name": "SWARNAVAHINI",
        "channel_id": "UCaIc6SgS90ud_RgMSC6hW_w",
        "title_keywords": ["Sinto", "සින්ටෝ"],
    },
    {
        "drama_key": "hiripoda_wessa",
        "drama_name": "Hiripoda Wessa (හිරිපොද වැස්ස)",
        "channel_key": "swarnavahini",
        "channel_name": "SWARNAVAHINI",
        "channel_id": "UCaIc6SgS90ud_RgMSC6hW_w",
        "title_keywords": ["Hiripoda Wessa", "හිරිපොද වැස්ස"],
    },
    {
        "drama_key": "maa",
        "drama_name": "Maa (මා)",
        "channel_key": "swarnavahini",
        "channel_name": "SWARNAVAHINI",
        "channel_id": "UCaIc6SgS90ud_RgMSC6hW_w",
        "title_keywords": ["Maa", "මා"],
    },
    {
        "drama_key": "pirimi_lamai",
        "drama_name": "Pirimi Lamai (පිරිමි ළමයි)",
        "channel_key": "swarnavahini",
        "channel_name": "SWARNAVAHINI",
        "channel_id": "UCaIc6SgS90ud_RgMSC6hW_w",
        "title_keywords": ["Pirimi Lamai", "පිරිමි ළමයි"],
    },
    {
        "drama_key": "jahuta",
        "drama_name": "Jahuta (ජහුටා)",
        "channel_key": "swarnavahini",
        "channel_name": "SWARNAVAHINI",
        "channel_id": "UCaIc6SgS90ud_RgMSC6hW_w",
        "title_keywords": ["Jahuta", "ජහුටා"],
    },
    {
        "drama_key": "taxikaraya",
        "drama_name": "Taxikaraya (ටැක්සිකාරයා)",
        "channel_key": "swarnavahini",
        "channel_name": "SWARNAVAHINI",
        "channel_id": "UCaIc6SgS90ud_RgMSC6hW_w",
        "title_keywords": ["Taxikaraya", "ටැක්සිකාරයා"],
    },
    {
        "drama_key": "jeewitheta_kotiyak",
        "drama_name": "Jeewitheta Kotiyak (ජීවිතේට කෝටියක්)",
        "channel_key": "swarnavahini",
        "channel_name": "SWARNAVAHINI",
        "channel_id": "UCaIc6SgS90ud_RgMSC6hW_w",
        "title_keywords": ["Jeewitheta Kotiyak", "ජීවිතේට කෝටියක්"],
    },

    # ================= ITN =================
    {
        "drama_key": "pahe_lamai",
        "drama_name": "Pahe Lamai (පහේ ළමයි)",
        "channel_key": "itn",
        "channel_name": "ITN",
        "channel_id": "UCQTcNhAZidy1i9wwmdgf2Lw",
        "title_keywords": ["Pahe Lamai", "පහේ ළමයි"],
    },
    {
        "drama_key": "mama_saha_oba",
        "drama_name": "Mama Saha Oba (මම සහ ඔබ)",
        "channel_key": "itn",
        "channel_name": "ITN",
        "channel_id": "UCQTcNhAZidy1i9wwmdgf2Lw",
        "title_keywords": ["Mama Saha Oba", "මම සහ ඔබ"],
    },
    {
        "drama_key": "sihineka_thaniwela",
        "drama_name": "Sihineka Thaniwela (සිහිනෙක තනිවෙලා)",
        "channel_key": "itn",
        "channel_name": "ITN",
        "channel_id": "UCQTcNhAZidy1i9wwmdgf2Lw",
        "title_keywords": ["Sihineka Thaniwela", "සිහිනෙක තනිවෙලා"],
    },
    {
        "drama_key": "visekari",
        "drama_name": "Visekari (විසේකාරී)",
        "channel_key": "itn",
        "channel_name": "ITN",
        "channel_id": "UCQTcNhAZidy1i9wwmdgf2Lw",
        "title_keywords": ["Visekari", "විසේකාරී"],
    },
    {
        "drama_key": "lbw",
        "drama_name": "LBW",
        "channel_key": "itn",
        "channel_name": "ITN",
        "channel_id": "UCQTcNhAZidy1i9wwmdgf2Lw",
        "title_keywords": ["LBW"],
    },
    {
        "drama_key": "patti_gedara",
        "drama_name": "Patti Gedara (පට්ටි ගෙදර)",
        "channel_key": "itn",
        "channel_name": "ITN",
        "channel_id": "UCQTcNhAZidy1i9wwmdgf2Lw",
        "title_keywords": ["Patti Gedara", "පට්ටි ගෙදර"],
    },

    # ================= RUPAVAHINI =================
    {
        "drama_key": "bedda_addara",
        "drama_name": "Bedda Addara (බැද්ද අද්දර)",
        "channel_key": "rupavahini",
        "channel_name": "RUPAVAHINI",
        "channel_id": "UCT83ymyAGm7Gnk_4ifxjxIA",
        "title_keywords": ["Bedda Addara", "බැද්ද අද්දර"],
    },
    {
        "drama_key": "adaraniya_minisek",
        "drama_name": "Adaraniya Minisek (ආදරණීය මිනිසෙක්)",
        "channel_key": "rupavahini",
        "channel_name": "RUPAVAHINI",
        "channel_id": "UCT83ymyAGm7Gnk_4ifxjxIA",
        "title_keywords": ["Adaraniya Minisek", "ආදරණීය මිනිසෙක්"],
    },
    {
        "drama_key": "dorakada_dewola",
        "drama_name": "Dorakada Dewola (දොරකඩ දෙවොල)",
        "channel_key": "rupavahini",
        "channel_name": "RUPAVAHINI",
        "channel_id": "UCT83ymyAGm7Gnk_4ifxjxIA",
        "title_keywords": ["Dorakada Dewola", "දොරකඩ දෙවොල"],
    },
]

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "")
DATABASE_URL = os.getenv("DATABASE_URL", "")

SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASS = os.getenv("SMTP_PASS", "")
REPORT_TO = os.getenv("REPORT_TO", "")
TZ = os.getenv("TZ", "Asia/Colombo")