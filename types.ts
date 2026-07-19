export interface Destination {
  id: string;
  title: string;
  subtitle: string;
  country: string;
  heroImage: string;
  category: 'Culture' | 'Nature' | 'Adventure' | 'Luxury';
  vibe: string;
  bestSeason: string;
  rating: number;
  readTime: string;
  author: {
    name: string;
    avatar: string;
    role: string;
  };
  intro: string;
  highlights: string[];
}

export interface ItineraryDay {
  day: number;
  title: string;
  description: string;
  spots: string[];
  tips: string;
  costEstimate: string;
  image: string;
}

export interface TravelArticle extends Destination {
  publishDate: string;
  content: string[];
  quote: string;
  quoteAuthor: string;
  itinerary: ItineraryDay[];
  budgetEstimates: {
    hotelBudget: number;
    diningBudget: number;
    activityBudget: number;
    flightBudget: number;
  };
  mapSpots: {
    name: string;
    lat: string;
    lng: string;
    x: number; // percentage coordinate for custom SVG map
    y: number; // percentage coordinate for custom SVG map
    description: string;
    image: string;
  }[];
  packingList: {
    category: string;
    items: string[];
  }[];
  weatherForecast: {
    season: string;
    temp: string;
    description: string;
    suitability: string;
    iconName: string;
  }[];
}

export interface SavedTrip {
  id: string;
  articleId: string;
  savedAt: string;
  customNotes?: string;
}

export interface Comment {
  id: string;
  userName: string;
  rating: number;
  content: string;
  date: string;
}
