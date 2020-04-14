require 'byebug'
require 'nokogori'
require 'selenium-webdriver'
require 'pdf-reader'
require 'humanizer'

SEC = 30
OFFSET = nil
SKIP_LIST = []

class Crawler
  ################################################

  # look for a word on the webpage
  def search_term(word='death')
    doc_text = @doc.text.encode('UTF-8', 'binary', invalid: :replace, undef: :replace, replace: '')
    if (i = (doc_text = ~ /#{word}/i)) && !(doc_text =~ /birth/i)
      puts "found #{word} in #{@st}"
      puts doc_text[(i-30)..(i+30)]
      return true
    end
    @driver.navigate.to @url
    if (i = (@driver.page_source =~ /#{word}/i)) && !(doc_text =~ /birth/i)
      puts "found #{word} in #{@st}"
      puts @driver.page_source[(i-30)..(i+30)]
      return true
    end
    false
  end

  # convert a string to an int
  def string_to_i(s)
    if !s
      byebug unless @auto_flas
      nil
    end
    return s if s.class == Integer
    if s.class == String
      s = s.strip.gsub(',','').gsub('-',' ').gsub(/\s+/,' ').downcase
      x = @h_numbers[s]
      return x if x
    end
    return 0 if s == "--"
    if s =~/^([0-9]+)\s?K/
      return $1.to_i * 1000
    end
    if s =~/Appx\. (.*)/
      s = $1
    elsif s =~ /~(.*)/
      s = $1
    elsif s =~ /App/
      byebug unless @auto_flag
    end
    case s.strip
    when "zero"
      0
    when "one"
      1
    when "two"
      2
    when "three"
      3
    when "four"
      4
    when "five"
      5
    when "six"
      6
    when "seven"
      7
    when "eight"
      8
    when "nine"
      9
    when "ten"
      10
    when 'eleven'
      11
    else
      if s =~ /in progress/
        nil
      else
        s = s.strip.gsub('‡','').gsub(',','')
        if s =~ /([0-9]+)/
          $1.to_i
        else
          puts "Please fix. Invalid number string"
          temp = nil
          byebug unless @auto_flag
          return temp
        end
      end
    end
  end

  def initialize
    profile =  Selenium::webdriver::Firefox::Profile.new
    #prodile.add_extension("/path/to/extension.xpi")
    profile['browser.download.dir'] = '~/Downloads'
    #profile['browser.download.folderList'] = 2
    profile['browser.helper.Apps.neverAsk.saveToDisk'] = "application/pdf, application/csv"
    profile['pdfjs.disabled'] = true
    options = Selenium::WebDriver::Firefox::Options.new(profile: profile)

    @driver = Selenium::WebDriver::Firefox::Opions.new(profile: profile)
    @path = 'data/'
    # load previous numbers
    lines = open('all.csv').readlines.map {|i| i.split("\t")}
    # previous state stats
    @h_prev = Hash.new({})
    lines.each do |st, tested, positive, deaths, junk|
      st.downcase!
      @h_prev[st] = {}
      @h_prev[st][:tested] = tested.to_i if tested.size > 0
    end

  end

  def crawl_page(url = @url)
    beginf
  end
end # Crawler class

