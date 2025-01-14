// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lex.Outputs
{

    /// <summary>
    /// A button to use on a response card used to gather slot values from a user.
    /// </summary>
    [OutputType]
    public sealed class BotButton
    {
        /// <summary>
        /// The text that appears on the button.
        /// </summary>
        public readonly string Text;
        /// <summary>
        /// The value returned to Amazon Lex when the user chooses this button.
        /// </summary>
        public readonly string Value;

        [OutputConstructor]
        private BotButton(
            string text,

            string value)
        {
            Text = text;
            Value = value;
        }
    }
}
