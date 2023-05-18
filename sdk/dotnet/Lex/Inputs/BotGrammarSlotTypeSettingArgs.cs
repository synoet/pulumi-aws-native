// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lex.Inputs
{

    /// <summary>
    /// Settings required for a slot type based on a grammar that you provide.
    /// </summary>
    public sealed class BotGrammarSlotTypeSettingArgs : global::Pulumi.ResourceArgs
    {
        [Input("source")]
        public Input<Inputs.BotGrammarSlotTypeSourceArgs>? Source { get; set; }

        public BotGrammarSlotTypeSettingArgs()
        {
        }
        public static new BotGrammarSlotTypeSettingArgs Empty => new BotGrammarSlotTypeSettingArgs();
    }
}
