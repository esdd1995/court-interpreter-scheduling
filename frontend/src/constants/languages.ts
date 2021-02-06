import { LanguageBase } from "./interfaces";

export const languages = [
  "Albanian",
  "Amharic",
  "Arabic",
  "ASL",
  "Bengali",
  "Bosnian",
  "Bulgarian",
  "Burmese",
  "Cambodian (Khmer)",
  "Cantonese",
  "CART",
  "Cebuano",
  "Chiu chow (Swatow)",
  "Croatian",
  "Czech",
  "Dari",
  "Dinka",
  "Dutch",
  "Farsi",
  "Farsi-persian",
  "Filipino",
  "French",
  "Fuquing",
  "Fuzhou",
  "German",
  "Greek",
  "Hakha chin",
  "Hindi",
  "Hungarian",
  "Igbo",
  "Ilocano",
  "Indonesian",
  "Italian",
  "Japanese",
  "Karen",
  "Kinyarwanda",
  "Kirundi",
  "Korean",
  "Kurdish",
  "Kurdish (Kurmanji)",
  "Kurdish (Sorani)",
  "Laotian",
  "Lithuanian",
  "Malay",
  "Malayalam",
  "Mandarin",
  "Nepali",
  "Oromo",
  "Pashto",
  "Polish",
  "Portuguese",
  "Punjabi",
  "Romanian",
  "Russian",
  "Serbian",
  "Shanghainese",
  "Sinhalese",
  "Slovak",
  "Somali",
  "Spanish",
  "Swahili",
  "Tagalog",
  "Tamil",
  "Teochew",
  "Thai",
  "Tigri(gna) (yna)",
  "Turkish",
  "Ukrainian",
  "Urdu",
  "Vietnamese",
  "Xinhui"
]

const languageByLowerCaseName: { [lowerCase: string]: string } = {}

for (const lang of languages) {
  languageByLowerCaseName[lang.toLowerCase()] = lang
}

export function fixLanguageName<T extends { languageName: string }>(toFix: T): T {
  return {
    ...toFix, 
    languageName: languageByLowerCaseName[toFix.languageName.toLowerCase()] || toFix.languageName
  }
}
