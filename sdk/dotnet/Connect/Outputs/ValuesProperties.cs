// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Connect.Outputs
{

    /// <summary>
    /// The values of a predefined attribute.
    /// </summary>
    [OutputType]
    public sealed class ValuesProperties
    {
        public readonly ImmutableArray<string> StringList;

        [OutputConstructor]
        private ValuesProperties(ImmutableArray<string> stringList)
        {
            StringList = stringList;
        }
    }
}
