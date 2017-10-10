from scraper import AccidentsScraper

output_file = "dataset.csv"

scraper = AccidentsScraper();
scraper.scrape();
scraper.data2csv(output_file);
