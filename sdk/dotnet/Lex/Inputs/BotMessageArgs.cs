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
    /// The primary message that Amazon Lex should send to the user.
    /// </summary>
    public sealed class BotMessageArgs : global::Pulumi.ResourceArgs
    {
        [Input("customPayload")]
        public Input<Inputs.BotCustomPayloadArgs>? CustomPayload { get; set; }

        [Input("imageResponseCard")]
        public Input<Inputs.BotImageResponseCardArgs>? ImageResponseCard { get; set; }

        [Input("plainTextMessage")]
        public Input<Inputs.BotPlainTextMessageArgs>? PlainTextMessage { get; set; }

        [Input("ssmlMessage")]
        public Input<Inputs.BotSSMLMessageArgs>? SsmlMessage { get; set; }

        public BotMessageArgs()
        {
        }
        public static new BotMessageArgs Empty => new BotMessageArgs();
    }
}
