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
    /// Specifies the text input specifications.
    /// </summary>
    [OutputType]
    public sealed class BotTextInputSpecification
    {
        /// <summary>
        /// Time for which a bot waits before re-prompting a customer for text input.
        /// </summary>
        public readonly int StartTimeoutMs;

        [OutputConstructor]
        private BotTextInputSpecification(int startTimeoutMs)
        {
            StartTimeoutMs = startTimeoutMs;
        }
    }
}
