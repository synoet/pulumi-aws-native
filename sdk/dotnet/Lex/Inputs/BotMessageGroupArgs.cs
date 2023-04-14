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
    /// One or more messages that Amazon Lex can send to the user.
    /// </summary>
    public sealed class BotMessageGroupArgs : global::Pulumi.ResourceArgs
    {
        [Input("message", required: true)]
        public Input<Inputs.BotMessageArgs> Message { get; set; } = null!;

        [Input("variations")]
        private InputList<Inputs.BotMessageArgs>? _variations;

        /// <summary>
        /// Message variations to send to the user.
        /// </summary>
        public InputList<Inputs.BotMessageArgs> Variations
        {
            get => _variations ?? (_variations = new InputList<Inputs.BotMessageArgs>());
            set => _variations = value;
        }

        public BotMessageGroupArgs()
        {
        }
        public static new BotMessageGroupArgs Empty => new BotMessageGroupArgs();
    }
}
