// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Outputs
{

    [OutputType]
    public sealed class EndpointConfigClarifyInferenceConfig
    {
        public readonly string? ContentTemplate;
        public readonly ImmutableArray<Outputs.EndpointConfigClarifyHeader> FeatureHeaders;
        public readonly ImmutableArray<Outputs.EndpointConfigClarifyFeatureType> FeatureTypes;
        public readonly string? FeaturesAttribute;
        public readonly string? LabelAttribute;
        public readonly ImmutableArray<Outputs.EndpointConfigClarifyHeader> LabelHeaders;
        public readonly int? LabelIndex;
        public readonly int? MaxPayloadInMb;
        public readonly int? MaxRecordCount;
        public readonly string? ProbabilityAttribute;
        public readonly int? ProbabilityIndex;

        [OutputConstructor]
        private EndpointConfigClarifyInferenceConfig(
            string? contentTemplate,

            ImmutableArray<Outputs.EndpointConfigClarifyHeader> featureHeaders,

            ImmutableArray<Outputs.EndpointConfigClarifyFeatureType> featureTypes,

            string? featuresAttribute,

            string? labelAttribute,

            ImmutableArray<Outputs.EndpointConfigClarifyHeader> labelHeaders,

            int? labelIndex,

            int? maxPayloadInMb,

            int? maxRecordCount,

            string? probabilityAttribute,

            int? probabilityIndex)
        {
            ContentTemplate = contentTemplate;
            FeatureHeaders = featureHeaders;
            FeatureTypes = featureTypes;
            FeaturesAttribute = featuresAttribute;
            LabelAttribute = labelAttribute;
            LabelHeaders = labelHeaders;
            LabelIndex = labelIndex;
            MaxPayloadInMb = maxPayloadInMb;
            MaxRecordCount = maxRecordCount;
            ProbabilityAttribute = probabilityAttribute;
            ProbabilityIndex = probabilityIndex;
        }
    }
}
