// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SSM.Outputs
{

    [OutputType]
    public sealed class DocumentAttachmentsSource
    {
        /// <summary>
        /// The key of a key-value pair that identifies the location of an attachment to a document.
        /// </summary>
        public readonly Pulumi.AwsNative.SSM.DocumentAttachmentsSourceKey? Key;
        /// <summary>
        /// The name of the document attachment file.
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// The value of a key-value pair that identifies the location of an attachment to a document. The format for Value depends on the type of key you specify.
        /// </summary>
        public readonly ImmutableArray<string> Values;

        [OutputConstructor]
        private DocumentAttachmentsSource(
            Pulumi.AwsNative.SSM.DocumentAttachmentsSourceKey? key,

            string? name,

            ImmutableArray<string> values)
        {
            Key = key;
            Name = name;
            Values = values;
        }
    }
}
