// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.FraudDetector.Outputs
{

    [OutputType]
    public sealed class DetectorTag
    {
        public readonly string Key;
        public readonly string Value;

        [OutputConstructor]
        private DetectorTag(
            string key,

            string value)
        {
            Key = key;
            Value = value;
        }
    }
}
