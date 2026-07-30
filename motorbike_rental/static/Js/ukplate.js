/**
 * UK Vehicle Registration Validation Module
 */

// Banned positional characters based on DVLA rules
const RESTRICTED_AREA_LETTERS = /[IQZ]/;
const RESTRICTED_SUFFIX_LETTERS = /[IQ]/;

// Core profanity/offensive substrings explicitly banned by DVLA across release windows
const BANNED_OFFENSIVE_PHRASES = [
  "ARS",
  "BOM",
  "BNP",
  "CNT",
  "CUM",
  "DCK",
  "FAG",
  "FCK",
  "FUK",
  "GAY",
  "HEL",
  "JAD",
  "KLL",
  "NAZ",
  "NGR",
  "NOB",
  "PAK",
  "PED",
  "SHG",
  "SHT",
  "SEX",
  "VAG",
  "WNK",
];

// Master Regular Expression covering Current, Prefix, Suffix, Dateless, and NI layouts
const UK_PLATE_LAYOUT_REGEX =
  /^(?:[A-Z]{2}[0-9]{2}[A-Z]{3}|[A-Z][0-9]{1,3}[A-Z]{3}|[A-Z]{3}[0-9]{1,3}[A-Z]|[0-9]{1,4}[A-Z]{1,3}|[A-Z]{1,3}[0-9]{1,4}|[A-Z]{3}[0-9]{1,4})$/;

/**
 * Strips whitespace and forces uppercase on an input string.
 * @param {string} value
 * @returns {string} Cleaned value
 */
export function sanitizeInput(value) {
  return (value || "").replace(/\s+/g, "").toUpperCase();
}

/**
 * Checks if the plate structure adheres to official DVLA positional character constraints.
 * @param {string} plate
 * @returns {boolean} True if structural layouts and character combinations are valid.
 */
function hasValidDvlaCharacters(plate) {
  if (plate.length === 7) {
    const areaCode = plate.slice(0, 2);
    const randomSuffix = plate.slice(4, 7);

    if (RESTRICTED_AREA_LETTERS.test(areaCode)) return false;
    if (RESTRICTED_SUFFIX_LETTERS.test(randomSuffix)) return false;
  }
  return true;
}

/**
 * Checks the string against blocked offensive phrases.
 * @param {string} plate
 * @returns {boolean} True if the plate contains no banned substrings.
 */
function hasNoOffensivePhrases(plate) {
  return !BANNED_OFFENSIVE_PHRASES.some((bannedWord) =>
    plate.includes(bannedWord),
  );
}

/**
 * Main Orchestrator: Validates a UK plate against all UI and regulatory filter rules.
 * @param {string} rawInput - The raw string from the text input field.
 * @returns {Object} Validation outcome object { isValid: boolean, cleanedValue?: string, error?: string }
 */
export function validateUkRegistration(rawInput) {
  const cleanedPlate = sanitizeInput(rawInput);

  if (!cleanedPlate) {
    return { isValid: false, error: "Registration field cannot be blank." };
  }

  if (!UK_PLATE_LAYOUT_REGEX.test(cleanedPlate)) {
    return { isValid: false, error: "Invalid UK registration format layout." };
  }

  if (!hasValidDvlaCharacters(cleanedPlate)) {
    return {
      isValid: false,
      error:
        "Invalid registration characters (I, Q, or Z restricted in this position).",
    };
  }

  if (!hasNoOffensivePhrases(cleanedPlate)) {
    return {
      isValid: false,
      error: "Registration matches a restricted or offensive DVLA pattern.",
    };
  }

  return {
    isValid: true,
    cleanedValue: cleanedPlate,
  };
}
