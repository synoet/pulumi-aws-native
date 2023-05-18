// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Outputs
{

    /// <summary>
    /// Intended usage of model.
    /// </summary>
    [OutputType]
    public sealed class ModelCardIntendedUses
    {
        public readonly string? ExplanationsForRiskRating;
        public readonly string? FactorsAffectingModelEfficiency;
        /// <summary>
        /// intended use cases.
        /// </summary>
        public readonly string? IntendedUses;
        /// <summary>
        /// Why the model was developed?
        /// </summary>
        public readonly string? PurposeOfModel;
        public readonly Pulumi.AwsNative.SageMaker.ModelCardRiskRating? RiskRating;

        [OutputConstructor]
        private ModelCardIntendedUses(
            string? explanationsForRiskRating,

            string? factorsAffectingModelEfficiency,

            string? intendedUses,

            string? purposeOfModel,

            Pulumi.AwsNative.SageMaker.ModelCardRiskRating? riskRating)
        {
            ExplanationsForRiskRating = explanationsForRiskRating;
            FactorsAffectingModelEfficiency = factorsAffectingModelEfficiency;
            IntendedUses = intendedUses;
            PurposeOfModel = purposeOfModel;
            RiskRating = riskRating;
        }
    }
}
