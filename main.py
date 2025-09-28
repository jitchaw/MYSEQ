#!/usr/bin/env python

import re
from argparse import ArgumentParser
from seqbio.calculation.SeqCal import gcContent, countBasesDict
from seqbio.pattern.SeqPattern import enzTargetsScan
from seqbio.seqMan.dnaconvert import reverseComplementSeq, dna2rna, dna2protein

#gcContent,countBases,transcription,translation,enzTargetsScan

def argparserLocal():
    parser = ArgumentParser(prog= 'myseq', description= 'Work with sequence')

    subparser = parser.add_subparsers(title= 'commands', description= 'Please choose command below:', dest= 'command')
    subparser.required = True

    gcContent_command = subparser.add_parser('gcContent', help= 'Calculate GC content')
    gcContent_command.add_argument('-s', '--seq', type= str, default= None, help= 'Provide sequence')

    countBases_command = subparser.add_parser('countBases', help= 'Count number of each base')
    countBases_command.add_argument('-s', '--seq', type= str, default= None, help= 'Provide sequence')
    countBases_command.add_argument('-r', '--revcomp', action= 'store_true', help= 'Convet DNA to reverse-complementary')

    transcription_command = subparser.add_parser('transcription', help= 'Convert DNA->RNA')
    transcription_command.add_argument('-s', '--seq', type= str, default= None, help= 'Provide sequence')
    transcription_command.add_argument('-r', '--revcomp', action= 'store_true', help= 'Convet DNA to reverse-complementary')

    translation_command = subparser.add_parser('translation', help= 'Convert DNA->Protein')
    translation_command.add_argument('-s', '--seq', type= str, default= None, help= 'Provide sequence')
    translation_command.add_argument('-r', '--revcomp', action= 'store_true', help= 'Convet DNA to reverse-complementary')
    
  

    enzTargetsScan_command = subparser.add_parser('enzTargetsScan', help= 'Find restriction enzyme')
    enzTargetsScan_command.add_argument('-s', '--seq', type= str, default= None, help= 'Provide sequence')
    enzTargetsScan_command.add_argument('-e', '--enz', type= str, default= None, help='Enzyme name')
    enzTargetsScan_command.add_argument('-r', '--revcomp', action= 'store_true', help= 'Convet DNA to reverse-complementary')
   
    return parser

def main():
    parser = argparserLocal()
    arg = parser.parse_args()

    if arg.seq == None:
        print("------\nError: You do not provide -s or --seq\n------\n")

    else:
        seq = arg.seq.upper()

    if arg.command == 'gcContent':
        if arg.seq == None:
            exit(parser.parse_args(['gcContent','-h']))
        print("Input",arg.seq,"\nGC content =", gcContent(seq) )

    elif arg.command == 'countBases':
        if arg.seq == None:
            exit(parser.parse_args(['countBases','-h']))
        
        elif arg.revcomp == False:
            print("Input",arg.seq,"\ncountBases =", countBasesDict(seq) )

        elif arg.revcomp == True:
            print("Input",arg.seq,"\ncountBases =", countBasesDict(reverseComplementSeq(seq)) )
        
    elif arg.command == 'transcription':
        if arg.seq == None:
            exit(parser.parse_args(['transcription','-h']))
        
        elif arg.revcomp == False:
            print("Input",arg.seq,"\nTranscription =", dna2rna(seq) )

        elif arg.revcomp == True:
            print("Input",arg.seq,"\nTranscription =", dna2rna(reverseComplementSeq(seq)) )

    elif arg.command == 'translation':
        if arg.seq == None:
            exit(parser.parse_args(['translation','-h']))
        
        elif arg.revcomp == False:
            print("Input",arg.seq,"\nTranslation =", dna2protein(seq) )

        elif arg.revcomp == True:
            print("Input",arg.seq,"\nTranslation =", dna2protein(reverseComplementSeq(seq)) )

    elif arg.command == 'enzTargetsScan':
        if arg.seq == None or arg.enz == None:
            exit(parser.parse_args(['enzTargetsScan','-h']))
        
        elif arg.revcomp == False:
            print("Input",arg.seq,"\nEcoRI sites =", enzTargetsScan(seq, arg.enz) )

        elif arg.revcomp == True:
            print("Input",arg.seq,"\nEcoRI sites =", enzTargetsScan(reverseComplementSeq(seq), arg.enz) )


if __name__ == "__main__":
    main()
        
