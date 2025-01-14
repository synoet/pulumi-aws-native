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
    /// The evaluation form question.
    /// </summary>
    [OutputType]
    public sealed class EvaluationFormQuestion
    {
        /// <summary>
        /// The instructions for the question.
        /// </summary>
        public readonly string? Instructions;
        /// <summary>
        /// The flag to enable not applicable answers to the question.
        /// </summary>
        public readonly bool? NotApplicableEnabled;
        /// <summary>
        /// The type of the question.
        /// </summary>
        public readonly Pulumi.AwsNative.Connect.EvaluationFormQuestionQuestionType QuestionType;
        /// <summary>
        /// The properties of the question
        /// </summary>
        public readonly Outputs.EvaluationFormQuestionTypeProperties? QuestionTypeProperties;
        /// <summary>
        /// The identifier used to reference the question.
        /// </summary>
        public readonly string RefId;
        /// <summary>
        /// The title of the question.
        /// </summary>
        public readonly string Title;
        /// <summary>
        /// The question weight used for scoring.
        /// </summary>
        public readonly double? Weight;

        [OutputConstructor]
        private EvaluationFormQuestion(
            string? instructions,

            bool? notApplicableEnabled,

            Pulumi.AwsNative.Connect.EvaluationFormQuestionQuestionType questionType,

            Outputs.EvaluationFormQuestionTypeProperties? questionTypeProperties,

            string refId,

            string title,

            double? weight)
        {
            Instructions = instructions;
            NotApplicableEnabled = notApplicableEnabled;
            QuestionType = questionType;
            QuestionTypeProperties = questionTypeProperties;
            RefId = refId;
            Title = title;
            Weight = weight;
        }
    }
}
