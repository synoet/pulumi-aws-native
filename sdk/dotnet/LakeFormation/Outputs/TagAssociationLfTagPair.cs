// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.LakeFormation.Outputs
{

    [OutputType]
    public sealed class TagAssociationLfTagPair
    {
        public readonly string CatalogId;
        public readonly string TagKey;
        public readonly ImmutableArray<string> TagValues;

        [OutputConstructor]
        private TagAssociationLfTagPair(
            string catalogId,

            string tagKey,

            ImmutableArray<string> tagValues)
        {
            CatalogId = catalogId;
            TagKey = tagKey;
            TagValues = tagValues;
        }
    }
}
