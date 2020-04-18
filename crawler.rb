require 'nokogiri'
require 'httparty'
require 'json'
require 'loofah'
require 'rails-html-sanitizer'

class Crawler
  def get_population
    # Sao Tome & Principe
    # Sao Tome and Principe
    # Ivory Coast
    # Côte d'Ivoire
    countries_map = ['São Tomé and Principe']

    page = HTTParty.get('https://www.worldometers.info/population/countries-in-africa-by-population/')

    parse_page = Nokogiri::HTML(page)

    tbody = parse_page.css('tbody')

    rows = tbody.css('tr')

    full_sanitizer = Rails::Html::FullSanitizer.new

    countries = {}

    rows.each do |row|
      cols = []
      tdata = row.css('td')
      tdata.each do |td|
        cols << full_sanitizer.sanitize(td.to_s)
      end

      country = {
        'population': cols[2],
        'yearly_change': cols[3],
        'net_change': cols[4],
        'density_pop_sqkm': cols[5],
        'land_area_sqkm': cols[6],
        'migrants_net': cols[7],
        'fert_rate': cols[8],
        'med_age': cols[9],
        'urban_pop': cols[10],
        'postion': cols[0],
        'world_share': cols[11]
      }

      countries[country[:name]] = country
    end

    puts countries
  end

  def get_cases
    # Sao Tome & Principe
    # Sao Tome and Principe
    # Ivory Coast
    # Côte d'Ivoire
    countries_map = ['São Tomé and Principe']

    page = HTTParty.get('https://www.worldometers.info/population/countries-in-africa-by-population/')

    parse_page = Nokogiri::HTML(page)

    tbody = parse_page.css('tbody')

    rows = tbody.css('tr')

    full_sanitizer = Rails::Html::FullSanitizer.new

    countries = {}

    rows.each do |row|
      cols = []
      tdata = row.css('td')
      tdata.each do |td|
        cols << full_sanitizer.sanitize(td.to_s)
      end

      country = {
        'population': cols[2],
        'yearly_change': cols[3],
        'net_change': cols[4],
        'density_pop_sqkm': cols[5],
        'land_area_sqkm': cols[6],
        'migrants_net': cols[7],
        'fert_rate': cols[8],
        'med_age': cols[9],
        'urban_pop': cols[10],
        'postion': cols[0],
        'world_share': cols[11]
      }

      countries[country[:name]] = country
    end

    puts countries
end