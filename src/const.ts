export const SITE_TITLE = 'Scorpio - Tech';
export const SITE_DESCRIPTION = 'Curated engineering tools and calculators for professionals.';
export const BASE_URL = '';

export const NAV_LINKS = [
  // { href: '/', label: 'Home' },
  // { href: '/calculator', label: 'Calculators' },
  { href: '/calculator2', label: 'Calculators' },
  { href: '/test', label: 'Test Page' },
  // { href: 'https://github.com/McKenzi84/ScorpioAstro', label: 'GitHub' },
];

export const LOGO_SVG = `
<svg width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M12 2L4.5 20.29L5.21 21L12 18L18.79 21L19.5 20.29L12 2Z" fill="#3B82F6"/>
  <path d="M12 18V21M12 18L18.79 21M12 18L5.21 21" stroke="#1D4ED8" stroke-width="2"/>
</svg>
`;

// Calculator definitions
export const CALCULATORS = [
  {
    id: 'dms-converter',
    title: 'Angles Converter',
    path: './calculators/DmsConverter.astro',
    description: 'Convert between decimal degrees and degrees/minutes/seconds',
  },
  // {
  //   id: 'dms-compact',
  //   title: 'DMS Converter (Compact)',
  //   path: './calculators/DmsConverterCompact.astro',
  //   description: 'Compact layout: decimal and DMS inputs side-by-side',
  // },

    {
    id: 'bar-weight',
    title: 'Bar Weight Calculator',
    path: './calculators/BarWeight.astro',
    description: 'Calculate the weight of a metal bar given its dimensions and density',
  },

  // Add more calculators here as they're created
  // {
  //   id: 'machining-calc',
  //   title: 'CNC & Machining',
  //   path: './calculators/MachiningCalc.astro',
  //   description: 'Professional machining calculations',
  // },
];


